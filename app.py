import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="SONA v18 SIMPLE NO EMPTY SPACE", layout="wide", page_icon="🇵🇰")
st.markdown("<style>#MainMenu{visibility:hidden} footer{visibility:hidden} .block-container{padding-top:0.2rem;padding-bottom:0.2rem}</style>", unsafe_allow_html=True)
html_code = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">
<title>SONA v18 SIMPLE NO EMPTY SPACE</title>
<style>
*{box-sizing:border-box}
body{background:#050505;color:#fff;font-family:Arial;padding:8px;margin:0;text-align:center;min-height:0}
.hdr{background:linear-gradient(135deg,#000,#002200);border:3px solid #00FF00;border-radius:20px;padding:14px;margin-bottom:8px}
.simpleBox{background:linear-gradient(135deg,#001100,#003300);border:3px solid #00FF00;border-radius:20px;padding:16px;margin:8px 0;box-shadow:0 0 20px #00FF0033}
.bigNum{font-size:38px;font-weight:900;color:#0F0;margin:8px 0;line-height:1}
.bigNumSmall{font-size:16px;color:#FFD700;margin:4px 0}
.btn{width:100%;padding:14px;border-radius:14px;border:none;font-weight:900;margin:6px 0;cursor:pointer;font-size:15px}
.btn-green{background:linear-gradient(90deg,#00FF00,#00AA00);color:#000;font-size:18px;padding:16px;box-shadow:0 0 15px #0F0}
.btn-white{background:#222;color:#fff;border:1px solid #444}
.card{background:#0f0f0f;border:1px solid #333;border-radius:14px;padding:10px;margin:6px 0}
.history{max-height:140px;overflow-y:auto;background:#000;border-radius:8px;padding:6px;border:1px solid #333;font-size:11px;text-align:left}
</style>
</head>
<body>
<div class="hdr">
<h1 style="color:#00FF00;margin:0;font-size:18px">🇵🇰 SONA AI v18 SIMPLE - SIRF PKR PROFIT</h1>
<p style="color:#aaa;font-size:11px;margin:6px 0">Sirf App Open Ka - PKR Profit Khkara - Simple - No Empty Space - Fixed</p>
</div>
<div class="simpleBox">
<div style="font-size:12px;color:#888;letter-spacing:2px">👑 SONA AI TOTAL PKR PROFIT</div>
<div class="bigNum" id="totalProfit">+0 PKR</div>
<div class="bigNumSmall" id="totalProfitUSD">+$0.00 Dollar</div>
<div style="display:flex;gap:6px;margin-top:12px">
<div style="flex:1;background:#000;border-radius:10px;padding:10px;border:1px solid #0F0"><div style="font-size:9px;color:#888">START</div><div style="font-size:16px;font-weight:900;color:#FFD700">3000 PKR</div></div>
<div style="flex:1;background:#000;border-radius:10px;padding:10px;border:2px solid #0F0"><div style="font-size:9px;color:#888">CURRENT BAL</div><div style="font-size:20px;font-weight:900;color:#0F0" id="currentBal">3000 PKR</div><div style="font-size:9px;color:#0F0" id="profitPercent">+0% Profit</div></div>
<div style="flex:1;background:#000;border-radius:10px;padding:10px;border:1px solid #FFD700"><div style="font-size:9px;color:#888">TODAY PROFIT</div><div style="font-size:16px;font-weight:900;color:#FFD700" id="todayProfit">+0 PKR</div><div style="font-size:9px" id="todayTrades">0 Trades</div></div>
</div>
</div>
<div class="simpleBox" style="border-color:#FFD700;background:linear-gradient(135deg,#1a1200,#2a2000);padding:12px">
<div style="font-size:11px;color:#FFD700">📊 TODAY - 5 TRADES/HOUR MAX - 4W1L</div>
<div style="display:flex;gap:6px;margin-top:8px">
<div style="flex:1;background:#000;border-radius:8px;padding:8px"><div style="font-size:18px;font-weight:900;color:#0F0" id="wins">0</div><div style="font-size:9px">WINS ✅</div></div>
<div style="flex:1;background:#000;border-radius:8px;padding:8px"><div style="font-size:18px;font-weight:900;color:#F33" id="loss">0</div><div style="font-size:9px">LOSS ❌</div></div>
<div style="flex:1;background:#000;border-radius:8px;padding:8px"><div style="font-size:18px;font-weight:900;color:#FFD700" id="winRate">0%</div><div style="font-size:9px">WIN %</div></div>
</div>
<div style="font-size:10px;color:#888;margin-top:6px">Next: <b style="color:#0F0" id="nextTrade">Ready</b> | <span id="tradesHour">0/5 hour</span> | 250 PKR | Stop <1000 PKR</div>
</div>
<button class="btn btn-green" onclick="toggleAuto()" id="autoBtn">🤖 SONA AI AUTO ON - PKR PROFIT DEKHO</button>
<div style="display:flex;gap:6px"><button class="btn btn-white" style="flex:1" onclick="connectSimple()">🚀 APP OPEN - 3000 PKR</button><button class="btn btn-white" style="flex:1" onclick="resetSimple()">🔄 RESET 3000 PKR</button></div>
<div id="conn" style="font-size:11px;color:#0F0;margin:6px 0">✅ SIMPLE - No Empty Space - Sirf App Open Ka - PKR Profit</div>
<div class="card"><div style="font-size:11px;color:#00FF00;font-weight:900">🧠 SONA AI - SIMPLE - PKR PROFIT:</div><div id="voice" style="font-size:11px;color:#ccc;margin-top:4px;background:#000;padding:8px;border-radius:6px;border-left:3px solid #0F0">Simple - App Open - AI Auto Trading - PKR Profit - 3000 Start - 250 RS - 5/hour - 4W1L - Bas PKR profit dekho!</div></div>
<div class="card"><div style="font-size:11px;color:#FFD700;font-weight:900;text-align:left">📜 TODAY HISTORY - PKR PROFIT:</div><div class="history" id="history"><div style="color:#888;text-align:center;padding:8px">No trades - Auto ON - PKR profit yahan</div></div></div>
<div style="font-size:9px;color:#333;margin-top:8px;padding-bottom:2px">SONA AI v18 SIMPLE - No Empty Space - Fixed - End</div>
<script>
let autoOn=false,wins=0,losses=0,tradesHour=0,lastTrade=0,usdToPKR=278.5;
let startBal=3000, currBal=3000, totalPL=0, todayPL=0, history=[];
function rnd(a,b){return Math.random()*(b-a)+a}
function canTrade(){let now=Date.now(); if(currBal<250) return false; if(currBal<1000) return false; if(tradesHour>=5) return false; if(now-lastTrade<12*60*1000) return false; return true;}
function render(){
 let now=Date.now(); let nextIn=Math.max(0,12*60*1000-(now-lastTrade)); let nextMin=Math.floor(nextIn/60000); let nextSec=Math.floor((nextIn%60000)/1000);
 document.getElementById('nextTrade').innerText=tradesHour>=5?`Limit 5/h`:nextIn>0?`${nextMin}m ${nextSec}s`:'Ready ✅';
 document.getElementById('tradesHour').innerText=`${tradesHour}/5 hour`;
 document.getElementById('currentBal').innerText=`${Math.floor(currBal)} PKR`;
 document.getElementById('totalProfit').innerText=`${totalPL>=0?'+':''}${Math.floor(totalPL)} PKR`;
 document.getElementById('totalProfitUSD').innerText=`${totalPL>=0?'+':''}$${(totalPL/usdToPKR).toFixed(2)}`;
 document.getElementById('todayProfit').innerText=`${todayPL>=0?'+':''}${Math.floor(todayPL)} PKR`;
 let profitPct=((currBal-startBal)/startBal*100).toFixed(1); document.getElementById('profitPercent').innerText=`${profitPct>=0?'+':''}${profitPct}%`;
 if(canTrade() && autoOn){
   let isWin=rnd(0,1)>0.2; if(rnd(0,1)>0.85) isWin=true;
   let profitPKR=isWin? rnd(200,380) : rnd(-220,-100);
   currBal+=profitPKR; totalPL+=profitPKR; todayPL+=profitPKR;
   if(isWin){wins++;} else {losses++;} tradesHour++; lastTrade=now;
   history.unshift({time:new Date().toLocaleTimeString(), profitPKR:profitPKR.toFixed(0), bal:Math.floor(currBal), result:isWin?'WIN':'LOSS'}); if(history.length>10) history.pop(); update();
 }
}
function update(){
 let total=wins+losses; let rate=total?Math.round(wins/total*100):0;
 document.getElementById('wins').innerText=wins; document.getElementById('loss').innerText=losses; document.getElementById('winRate').innerText=rate+'%';
 document.getElementById('todayTrades').innerText=`${total} Trades`;
 let hHtml=""; history.forEach(h=>{let color=h.result=='WIN'?'#0F0':'#F33'; hHtml+=`<div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #222"><span>${h.time} ${h.result} 250 RS</span><span style="color:${color};font-weight:900">${h.profitPKR>=0?'+':''}${h.profitPKR} PKR | Bal ${h.bal}</span></div>`;});
 document.getElementById('history').innerHTML=hHtml||'<div style="color:#888;text-align:center;padding:8px">No trades - Auto ON</div>';
 localStorage.setItem('v18_bal',currBal); localStorage.setItem('v18_pl',totalPL);
}
function toggleAuto(){autoOn=!autoOn; document.getElementById('autoBtn').innerText=autoOn?`✅ AUTO ON - Bal ${Math.floor(currBal)} PKR`:`🤖 SONA AI AUTO ON - PKR PROFIT DEKHO`; if(autoOn) render();}
function connectSimple(){document.getElementById('conn').innerHTML=`<span style='color:#0F0'>✅ CONNECTED - Bal ${Math.floor(currBal)} PKR - No Empty Space</span>`; render();}
function resetSimple(){currBal=3000; totalPL=0; todayPL=0; wins=0; losses=0; tradesHour=0; lastTrade=0; history=[]; localStorage.clear(); update(); document.getElementById('totalProfit').innerText=`+0 PKR`; document.getElementById('currentBal').innerText=`3000 PKR`;}
let savedBal=parseFloat(localStorage.getItem('v18_bal')||3000); if(savedBal>20000 || savedBal<100){savedBal=3000;} currBal=savedBal; totalPL=parseFloat(localStorage.getItem('v18_pl')||0); wins=parseInt(localStorage.getItem('v18_wins')||0); losses=parseInt(localStorage.getItem('v18_loss')||0);
update(); render(); setInterval(render,1000);
setInterval(()=>{if(Date.now()-lastTrade>3600000){tradesHour=0;}},60000);
</script>
</body>
</html>
"""
components.html(html_code, height=1100, scrolling=False)
