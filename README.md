# Diff Auto Switch Smart and Solaris for nvOC mining OS

Put both DIFF_AUTO_SWITCH and DIFF_AUTO_SWITCH.py in /home/m1/

Edit /home/m1/1bash and add :
```
 
DIFF_AUTO_SWITCH="YES"
DIFF_AUTO_SWITCH_SYNC_INTERVAL="3" # Time to sync with DIFF for best coin
```

Edit /home/m1/3main and add these lines somewhere  after Maxximus007_AUTO_TEMPERATURE_CONTROL ( easier to find "SALFTER_NICEHASH_PROFIT_SWITCHING" and add before it:
```
if [ $DIFF_AUTO_SWITCH == "YES" ]
then
HCD='/home/m1/DIFF_AUTO_SWITCH'
running=$(ps -ef | awk '$NF~"DIFF_AUTO_SWITCH" {print $2}')
if [ "$running" == "" ]
then
guake -n $HCD -r DIFF_AUTO_SWITCH -e "bash /home/m1/DIFF_AUTO_SWITCH"
running=""
fi
fi
```
Install requests python module with :
```
sudo apt install  python-requests

Now you can start diff auto switch with
```bash DIFF_AUTO_SWITCH &```
