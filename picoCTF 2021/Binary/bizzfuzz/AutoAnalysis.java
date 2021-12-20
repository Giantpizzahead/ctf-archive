//Auto analyze the binary
//@author 
//@category Analysis
//@keybinding 
//@menupath 
//@toolbar 

import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.*;
import ghidra.program.model.util.*;
import ghidra.program.model.reloc.*;
import ghidra.program.model.data.*;
import ghidra.program.model.block.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.scalar.*;
import ghidra.program.model.mem.*;
import ghidra.program.model.lang.*;
import ghidra.program.model.pcode.*;
import ghidra.program.model.address.*;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;
import java.util.regex.*;

public class AutoAnalysis extends GhidraScript {
	
	private void analyzeGets(String name, String code) throws Exception {
		// Get buffer size
		int startLoc = code.indexOf('[');
		int endLoc = code.indexOf(']');
		int bufSize = Integer.parseInt(code.substring(startLoc+1, endLoc));
		// Look for overflows
		Pattern pattern = Pattern.compile(",(.*),\\*\\(FILE \\*\\*\\)");
		Matcher matcher = pattern.matcher(code);
		int bestOverflow = 0;
		while (matcher.find()) {
			String amountStr = matcher.group(1);
			int amount = 0;
			if (amountStr.indexOf('x') != -1) {
				// Hex
				amount = Integer.parseInt(amountStr.substring(2), 16);
			} else {
				// Decimal
				amount = Integer.parseInt(amountStr);
			}
			if (amount - bufSize > bestOverflow) {
				bestOverflow = amount - bufSize;
			}
			// println(Integer.toString(amount));
		}
		// println("bufSize: " + bufSize);
		if (bestOverflow != 0) {
			printerr(name + ": OVERFLOW " + bestOverflow);
		}
	}
	
	private HashMap<String, String> vis = new HashMap<>();
	
	private void findChain(Function start) throws Exception {
		Queue<Function> q = new LinkedList<>();
		q.add(start);
		vis.put(start.getName(), "START");
		while (!q.isEmpty()) {
			Function f = q.poll();
			println("On " + f.getName() + "[" + q.size() + "]");
			if (f.getName().equals("main")) {
				// Found main function
				break;
			}
			Set<Function> calling = f.getCallingFunctions(monitor);
			for (Function g : calling) {
				if (vis.containsKey(g.getName())) continue;  // Already visited
				vis.put(g.getName(), f.getName());
				q.add(g);
			}
		}
		// Backtrace
		printerr("Call path:");
		String curr = "main";
		while (!curr.equals("START")) {
			printerr(curr);
			curr = vis.get(curr);
		}
	}
	
	private void analyzeFunction(Function f) {
		try {
			// Decompile the function
			DecompInterface di = new DecompInterface();
			di.openProgram(currentProgram);
			DecompileResults dr = di.decompileFunction(f, 30, monitor);
			if (!dr.decompileCompleted()) throw new Exception("Decompile of " + f.getName() + " FAILED");
			String code = dr.getDecompiledFunction().getC();
			
			// Two types of functions
			if (code.indexOf("PTR_stdin") != -1) {
				// println(f.getName() + " [fgets]");
				analyzeGets(f.getName(), code);
			}
			if (code.indexOf("uVar1") != -1) {
				// println(f.getName() + " [chain]");
				// analyzeChain(f.getName(), code);
			}
		} catch (Exception e) {
			printerr("ERROR analyzing function " + f.getName() + ", please check manually!");
		}
	}

    public void run() throws Exception {
    	FunctionManager fm = currentProgram.getFunctionManager();
    	FunctionIterator functions = fm.getFunctions(true);
    	int cnt = 0;
    	for (Function f : functions) {
    		String name = f.getName();
//    		if (name.startsWith("FUN")) {
//    			// Analyze this
//    			analyzeFunction(f);
//    			if (cnt++ % 50 == 0) println("On function " + cnt);
//    		}
    		if (name.startsWith("OVERFLOW")) {
    			findChain(f);
    			break;
    		}
    	}
    }

}
