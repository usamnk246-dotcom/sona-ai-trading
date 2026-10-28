import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SONA v21.9 BETTER CODE", layout="wide", page_icon="💎")
st.markdown("<style>#MainMenu{visibility:hidden}footer{visibility:hidden}.block-container{padding:0;margin:0}header{visibility:hidden}.stApp{padding-top:0}iframe{margin:0}</style>", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>SONA v21.9 BETTER CODE</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}body{background:#050505;color:#fff;font-family:Arial;padding:6px;text-align:center;overflow-x:hidden}
.hdr{background:linear-gradient(135deg,#000,#001a00);border:2px solid #0F0;border-radius:12px;padding:10px;margin-bottom:6px}
.simpleBox{background:linear-gradient(135deg,#001100,#002200);border:2px solid #0F0;border-radius:12px;padding:10px;margin:6px 0}
.bigNum{font-size:32px;font-weight:900;color:#0F0;margin:4px 0}
.btn{width:100%;padding:10px;border-radius:8px;border:none;font-weight:900;margin:3px 0;cursor:pointer;font-size:11px}
.btn-green{background:linear-gradient(90deg,#0F0,#FFD700);color:#000;box-shadow:0 0 8px #0F0}
.btn-green.off{background:#333;color:#888;border:1px solid #555;box-shadow:none}
.btn-white{background:#1a1a1a;color:#fff;border:1px solid #444;font-size:10px}
.btn-tab{flex:1;padding:8px;border-radius:8px;border:2px solid #333;background:#111;color:#888;font-weight:900;cursor:pointer;font-size:9px}
.btn-tab.active{background:linear-gradient(90deg,#0F0,#00cc00);color:#000;border-color:#0F0}
.card{background:#0f0f0f;border:1px solid #333;border-radius:10px;padding:8px;margin:5px 0;text-align:left}
.history{max-height:100px;overflow-y:auto;background:#000;border-radius:6px;padding:4px;border:1px solid #333;font-size:9px}
.tab-content{display:none}.tab-content.active{display:block}
.detail{font-size:9px;color:#ccc;background:#000;padding:6px;border-radius:5px;margin:4px 0;border-left:3px solid #0F0;text-align:left}
.detail-gold{border-left-color:#FFD700;background:#1a1a00}
.candle-bar{height:14px;background:#222;border-radius:7px;overflow:hidden;margin:6px 0;border:1px solid #444}
.candle-fill{height:100%;background:linear-gradient(90deg,#0F0,#FFD700);width:0%;transition:width 0.5s linear}
.candle-timer{font-size:12px;color:#FFD700;font-weight:900;margin:4px 0}
.trade-status{font-size:11px;padding:6px;border-radius:7px;margin:4px 0;font-weight:900}
.status-running{background:#001a00;border:2px solid #0F0;color:#0F0;animation:pulse 1s infinite}
.status-waiting{background:#1a1a00;border:1px solid #FFD700;color:#FFD700}
.status-closed{background:#0a0a0a;border:1px solid #444;color:#aaa}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.7}}
.debug{font-size:8px;color:#777;background:#000;padding:4px;border-radius:4px;margin:3px 0;text-align:left;border:1px dashed #333}
</style></head>
<body>
<div class="hdr"><h1 style="color:#0F0;margin:0;font-size:13px">SONA AI v21.9 - BETTER CODE - DETAILED - 5 TRADE/HOUR</h1></div>
<div class="simpleBox"><div style="font-size:9px;color:#888">SONA AI - TOTAL PROFIT - BETTER CODE</div><div class="bigNum" id="totalProfit">+621 PKR</div><div style="font-size:12px;color:#FFD700" id="totalProfitUSD">+$2.23 - +20.7% - Better Code</div>
<div style="display:flex;gap:4px;margin-top:6px"><div style="flex:1;background:#000;border-radius:8px;padding:6px;border:1px solid #0F0"><div style="font-size:6px;color:#888">START</div><div style="font-size:13px;font-weight:900;color:#FFD700">3000 PKR</div></div><div style="flex:1;background:#000;border-radius:8px;padding:6px;border:2px solid #0F0"><div style="font-size:6px;color:#888">CURRENT BAL</div><div style="font-size:16px;font-weight:900;color:#0F0" id="currentBal">3621 PKR</div></div><div style="flex:1;background:#000;border-radius:8px;padding:6px;border:1px solid #FFD700"><div style="font-size:6px;color:#888">TODAY PROFIT</div><div style="font-size:13px;font-weight:900;color:#FFD700" id="todayProfit">+621 PKR</div><div style="font-size:6px" id="todayTrades">12 Trades</div></div></div></div>
<div class="simpleBox" style="border-color:#FFD700;background:#1a3300"><div style="font-size:10px;color:#0F0;font-weight:900">5 TRADES/HOUR - 3 WIN 1 LOSS - 12 MIN COOLDOWN - BETTER CODE</div>
<div style="display:flex;gap:4px;margin-top:6px"><div style="flex:1;background:#000;border-radius:8px;padding:6px;border:2px solid #0F0"><div style="font-size:16px;font-weight:900;color:#0F0" id="wins">9</div><div style="font-size:7px">WINS 75% - Better</div></div><div style="flex:1;background:#000;border-radius:8px;padding:6px"><div style="font-size:16px;font-weight:900;color:#F33" id="loss">3</div><div style="font-size:7px">LOSS 25% - Better</div></div><div style="flex:1;background:#000;border-radius:8px;padding:6px;border:2px solid #FFD700"><div style="font-size:18px;font-weight:900;color:#FFD700" id="winRate">75%</div><div style="font-size:7px">WIN % - Better</div></div></div>
<div class="trade-status status-waiting" id="tradeStatus">WAITING - Next Trade Ready - Better Code</div>
<div class="candle-bar"><div class="candle-fill" id="candleFill"></div></div>
<div class="candle-timer" id="candleTimer">Candle: Ready - Better Code</div>
<div class="debug" id="debugInfo">Debug: tradesHour 0/5 | cooldown 12min | tradeActive false | Better Code</div>
<div style="font-size:8px;color:#888">Pattern: <b style="color:#0F0">WIN WIN WIN LOSS</b> | Next: <b style="color:#0F0" id="nextTrade">WIN (1/3) - Ready</b> | <span id="tradesHour">0/5</span> | <span id="nextIn">Ready</span> | <span id="autoStatus">AUTO ON</span></div></div>
<div style="display:flex;gap:4px;margin:5px 0"><button class="btn-tab active" id="tabSimple" onclick="switchTab('simple')">BETTER CODE (Detail)</button><button class="btn-tab" id="tabNexus" onclick="switchTab('nexus')">CODE LOGIC</button><button class="btn-tab" id="tabRisk" onclick="switchTab('risk')">RISK (Detail)</button></div>
<div id="contentSimple" class="tab-content active"><button class="btn btn-green" id="autoBtn" onclick="toggleAuto()">AUTO ON - Bal 3621 - Profit 621 - BETTER CODE</button><div style="display:flex;gap:4px"><button class="btn btn-white" style="flex:1" onclick="openApp()">APP OPEN - 3000 PKR</button><button class="btn btn-white" style="flex:1" onclick="resetAll()">RESET 3000 PKR</button></div><div style="display:flex;gap:4px"><button class="btn btn-green" style="flex:1" onclick="manualTrade()">MANUAL TRADE - 250 PKR - Better</button><button class="btn btn-white" style="flex:1" onclick="clearCooldown()">CLEAR COOLDOWN - FORCE FIX</button></div>
<div class="detail"><b>BETTER CODE v21.9 - Details:</b> Constants: fixedDuration=60s, cooldown=12min (60/5), hourStart | State: currBal, wins, tradesHour, patternCounter | Pattern: %4<3=WIN else LOSS | 5 Trade/Hour: 12min cooldown + hour reset | Trade: start->60s->close->profit +260-390/-50-90 | Auto Recover 65s force close - fixes 5h stuck bug</div></div>
<div class="card"><div class="history" id="history"></div></div>
<script>
function switchTab(tab){document.querySelectorAll('.btn-tab').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active'));document.getElementById('tab'+tab.charAt(0).toUpperCase()+tab.slice(1)).classList.add('active');document.getElementById('content'+tab.charAt(0).toUpperCase()+tab.slice(1)).classList.add('active');}
let autoOn=true,wins=9,losses=3,tradesHour=0,lastTrade=0,usdToPKR=278.5,startBal=3000,currBal=3621,totalPL=621,patternCounter=12,historyData=[],tradeActive=false,tradeEndTime=0,tradeStartTime=0,fixedDuration=60000,cooldownDuration=720000,hourStart=Date.now();
function rnd(a,b){return Math.random()*(b-a)+a}
function saveState(){try{localStorage.setItem('sona_v219_bal',currBal);localStorage.setItem('sona_v219_pl',totalPL);localStorage.setItem('sona_v219_wins',wins);localStorage.setItem('sona_v219_losses',losses);localStorage.setItem('sona_v219_pattern',patternCounter);localStorage.setItem('sona_v219_tradesHour',tradesHour);localStorage.setItem('sona_v219_lastTrade',lastTrade);localStorage.setItem('sona_v219_hourStart',hourStart);localStorage.setItem('sona_v219_history',JSON.stringify(historyData));}catch(e){}}
function loadState(){try{let b=localStorage.getItem('sona_v219_bal');if(b!==null){currBal=parseFloat(b);totalPL=parseFloat(localStorage.getItem('sona_v219_pl')||621);wins=parseInt(localStorage.getItem('sona_v219_wins')||9);losses=parseInt(localStorage.getItem('sona_v219_losses')||3);patternCounter=parseInt(localStorage.getItem('sona_v219_pattern')||12);tradesHour=parseInt(localStorage.getItem('sona_v219_tradesHour')||0);lastTrade=parseInt(localStorage.getItem('sona_v219_lastTrade')||0);hourStart=parseInt(localStorage.getItem('sona_v219_hourStart')||Date.now());let h=localStorage.getItem('sona_v219_history');if(h){historyData=JSON.parse(h);}}}catch(e){}}
function getNextResult(){return (patternCounter % 4) < 3;}
function checkHourReset(){let now=Date.now();if(now-hourStart>=3600000){tradesHour=0;hourStart=now;saveState();}}
function canStartNewTrade(){checkHourReset();if(tradeActive)return false;if(currBal<250)return false;if(currBal<1000)return false;if(tradesHour>=5)return false;if(lastTrade!=0&&Date.now()-lastTrade<cooldownDuration)return false;return true;}
function startTrade(isManual=false){checkHourReset();if(!canStartNewTrade()){if(isManual){if(tradeActive)alert('Trade running - Wait 65s auto recover');else if(tradesHour>=5)alert('5/h limit - Wait 1h');else{let r=Math.max(0,cooldownDuration-(Date.now()-lastTrade));alert('Cooldown - Next in '+Math.floor(r/60000)+'m '+Math.floor((r%60000)/1000)+'s');}}return;}tradeActive=true;tradeStartTime=Date.now();tradeEndTime=tradeStartTime+fixedDuration;document.getElementById('tradeStatus').className='trade-status status-running';document.getElementById('tradeStatus').innerText='TRADE RUNNING - 60s - '+(getNextResult()?'WIN':'LOSS')+' expected';saveState();}
function closeTrade(){let isWin=getNextResult();patternCounter++;let p=isWin?rnd(260,390):rnd(-50,-90);currBal+=p;totalPL+=p;if(isWin)wins++;else losses++;tradesHour++;lastTrade=Date.now();tradeActive=false;tradeEndTime=0;tradeStartTime=0;let t=new Date().toLocaleTimeString();historyData.unshift({time:t,result:isWin?'WIN':'LOSS',profit:p.toFixed(0),bal:Math.floor(currBal)});if(historyData.length>15)historyData.pop();updateHistory();saveState();document.getElementById('tradeStatus').className='trade-status status-closed';document.getElementById('tradeStatus').innerText='TRADE CLOSED - '+(isWin?'WIN':'LOSS')+' '+(p>=0?'+':'')+p.toFixed(0)+' PKR - Next in 12min';document.getElementById('candleFill').style.width='0%';render();}
function toggleAuto(){autoOn=!autoOn;let b=document.getElementById('autoBtn');if(autoOn){b.className='btn btn-green';b.innerText='AUTO ON - Bal '+Math.floor(currBal)+' - Profit '+Math.floor(totalPL)+' - BETTER CODE';}else{b.className='btn btn-green off';b.innerText='AUTO OFF - Bal '+Math.floor(currBal)+' - Profit '+Math.floor(totalPL);}}
function manualTrade(){startTrade(true);}function clearCooldown(){lastTrade=0;tradesHour=0;hourStart=Date.now();tradeActive=false;tradeEndTime=0;tradeStartTime=0;saveState();alert('FORCE FIXED - Better Code - Ready!');render();}
function render(){let now=Date.now();checkHourReset();if(tradeActive){let e=now-tradeStartTime;if(e>65000){closeTrade();return;}let rem=Math.max(0,tradeEndTime-now);let prog=(e/fixedDuration)*100;document.getElementById('candleFill').style.width=Math.min(100,prog)+'%';document.getElementById('candleTimer').innerText='Candle: '+Math.ceil(rem/1000)+'s remaining - '+Math.floor(prog)+'% - Better Code';if(rem<=0){closeTrade();return;}}else{let nextIn=lastTrade==0?0:Math.max(0,cooldownDuration-(now-lastTrade));document.getElementById('nextIn').innerText=lastTrade==0?'Ready':tradesHour>=5?'5/h limit - '+(60-Math.floor((now-hourStart)/60000))+'m':Math.floor(nextIn/60000)+'m '+Math.floor((nextIn%60000)/1000)+'s left';}document.getElementById('tradesHour').innerText=tradesHour+'/5';document.getElementById('currentBal').innerText=Math.floor(currBal)+' PKR';document.getElementById('totalProfit').innerText=(totalPL>=0?'+':'')+Math.floor(totalPL)+' PKR';document.getElementById('totalProfitUSD').innerText=(totalPL>=0?'+':'')+'$'+(totalPL/usdToPKR).toFixed(2)+' - Better Code';document.getElementById('todayProfit').innerText=(totalPL>=0?'+':'')+Math.floor(totalPL)+' PKR';document.getElementById('profitPercent').innerText='+'+((currBal-startBal)/startBal*100).toFixed(1)+'%';document.getElementById('debugInfo').innerText='Debug: tradesHour '+tradesHour+'/5 | lastTrade '+(lastTrade==0?'0':Math.floor((now-lastTrade)/1000)+'s ago')+' | 12min | active '+tradeActive+' | Better Code';if(canStartNewTrade()&&autoOn&&!tradeActive){startTrade(false);}}
function updateHistory(){let total=wins+losses;let rate=total?Math.round(wins/total*100):75;document.getElementById('wins').innerText=wins;document.getElementById('loss').innerText=losses;document.getElementById('winRate').innerText=rate+'%';document.getElementById('todayTrades').innerText=total+' Trades';let hHtml="";historyData.forEach(h=>{let c=h.result=='WIN'?'#0F0':'#F33';hHtml+='<div style="display:flex;justify-content:space-between;padding:2px 0;border-bottom:1px solid #222"><span>'+h.time+' '+h.result+' 250 RS</span><span style="color:'+c+';font-weight:900">'+(Number(h.profit)>=0?'+':'')+h.profit+' PKR | Bal '+h.bal+'</span></div>';});document.getElementById('history').innerHTML=hHtml;}
function openApp(){alert('APP OPEN - BETTER CODE - 5 Trade/Hour!');}function resetAll(){if(!confirm('Reset?'))return;localStorage.clear();currBal=3000;totalPL=0;wins=0;losses=0;tradesHour=0;lastTrade=0;hourStart=Date.now();patternCounter=0;historyData=[];tradeActive=false;updateHistory();render();}
loadState();updateHistory();render();setInterval(render,500);
</script>
</body>
</html>
"""

components.html(html_code, height=1650, scrolling=False)
