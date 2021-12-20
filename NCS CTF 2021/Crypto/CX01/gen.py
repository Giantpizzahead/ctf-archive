from mnemonic import Mnemonic

mnemo = Mnemonic("english")

m_raw = 'nature midnight buzz toe sleep fence kiwi ivory excuse system'
seed_start = '131c553f7fb4127e7b2b346991dd92'
with open('wordlist.txt', 'r') as fin:
    wordlist = fin.read().split()

# Try all sets of 2 codewords
for i in range(639, len(wordlist)):
    if len(wordlist[i]) != 4: continue
    print('On {}/{}'.format(i+1, len(wordlist)))
    for j in range(len(wordlist)):
        if len(wordlist[j]) != 6: continue
        words = m_raw + ' {} {}'.format(wordlist[i], wordlist[j])
        seed = mnemo.to_seed(words, passphrase='').hex()
        if seed.startswith(seed_start):
            print('*** VALID WORDLIST FOUND ***')
            print(words)
            print(seed)
            input()

# nature midnight buzz toe sleep fence kiwi ivory excuse system exit filter
# https://iancoleman.io/bip39/
# 1BvBytaskgTZkJEEUEkBxv6kDWbAKabnmK