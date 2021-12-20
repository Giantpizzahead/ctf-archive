$input = "./input.txt"

$out = Get-Content -Path $input
$enc = [System.IO.File]::ReadAllBytes("$input")  # enc contains an array of bytes
$encoding = [system.Text.Encoding]::UTF8
$total = 264
$t = ($total + 1) * 5  # 1325
$numLength = ($total * 30 ) + $t  # 9245
if (0)#$out.Length -gt 5 -or $enc.count -ne $numLength)  # if out.Length > 5 or enc.count != numLength, exit
{
  Write-Output "Wrong format 5"
  Exit
}

else
{
  for($i=0; $i -lt $enc.count ; $i++)  # Checks if all bytes are 1, 0, newline, carriage return, or space
  {
    if (($enc[$i] -ne 49) -and ($enc[$i] -ne 48) -and ($enc[$i] -ne 10) -and ($enc[$i] -ne 13) -and ($enc[$i] -ne 32))
    {
      Write-Output "Wrong format 1/0/"
      Exit
    }
  }
}

# Splits the input into 6-character blocks with only 0s and 1s
$blocks = @{}
for ($i=0; $i -lt $out.Length ; $i++)
{
  $r = $out[$i].Split(" ")
  Write-Output "r = $i"
  Write-Output $r
  if ($i -gt 0)
  {
    for ($j=0; $j -lt $r.Length ; $j++)
    {
    if ($r[$j].Length -ne 6)
    {
      Write-Output "Wrong Format 6" $r[$j].Length
      Exit
    }
      $blocks[$j] += $r[$j]
    }
  }
  else
  {
    for ($j=0; $j -lt $r.Length ; $j++)
    {
    if ($r[$j].Length -ne 6)
    {
      Write-Output "Wrong Format 6" $r[$j].Length
      Exit
    }
      $blocks[$j] = @()
      $blocks[$j] += $r[$j]
    }
  }

}


function Exit  {
  exit
}


function Random-Gen {
  $list1 = @()
  for ($i=1; $i -lt ($blocks.count + 1); $i++)
  {
    $y = ((($i * 327) % 681 ) + 344) % 313
    $list1 += $y
  }
  return $list1
}


function Scramble {
    param (
        $block,
        $seed
    )
    $raw = [system.String]::Join("", $block)
    $bm = "10 " * $raw.Length
    $bm = $bm.Split(" ")
    Write-Host "bm = $bm"
    for ($i=0; $i -lt $raw.Length ; $i++)
    {

      $y = ($i * $seed) % $raw.Length
      $n = $bm[$y]
      while ($n -ne "10")
      {
        $y = ($y + 1) % $raw.Length
        $n = $bm[$y]
      }
      if ($raw[$i] -eq "1" )
      {
        $n = "11"
      }
      else
      {
      $n = "00"
      }
      $bm[$y] = $n
    }
    $raw2 = [system.String]::Join("", $bm)
    Write-Host "raw2 = $raw2"
    $b = [convert]::ToInt64($raw2,2)
    return $b
}


$result = 0
$seeds = @()
for ($i=1; $i -lt ($blocks.count +1); $i++)
{
  $seeds += ($i * 127) % 500
}

$randoms = Random-Gen
$output_file = @()
for ($i=0; $i -lt $blocks.count ; $i++)
{
  Write-Output "----- Block $i -----" 
  Write-Output "Block: $($blocks[$i])"
  Write-Output "Seed:  $($seeds[$i])"
  Write-Output "Rand:  $($randoms[$i])"
  $fun = Scramble -block $blocks[$i] -seed $seeds[$i]
  Write-Output "Fun:   $fun"
  Write-Output ""
  $result = $fun -bxor $result -bxor $randoms[$i]
  $output_file += $result
}
  Add-Content -Path output.txt -Value $output_file