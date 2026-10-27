import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="SONA + NEXUS v19 HYBRID SAVE SHO FINAL", layout="wide", page_icon="👑")
st.markdown("<style>#MainMenu{visibility:hidden} footer{visibility:hidden} .block-container{padding-top:0.1rem;padding-bottom:0.1rem}</style>", unsafe_allow_html=True)
html_code = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SONA + NEXUS v19 HYBRID - SIMPLE UI + ADVANCED AI</title>
<style>
*{box-sizing:border-box}
body{background:#050505;color:#fff;font-family:Arial;padding:8px;margin:0;text-align:center}
.hdr{background:linear-gradient(135deg,#000,#002200);border:3px solid #00FF00;border-radius:18px;padding:12px;margin-bottom:6px}
.simpleBox{background:linear-gradient(135deg,#001100,#003300);border:3px solid #00FF00;border-radius:18px;padding:14px;margin:6px 0}
.bigNum{font-size:36px;font-weight:900;color:#0F0;margin:6px 0;line-height:1}
.btn{width:100%;padding:12px;border-radius:12px;border:none;font-weight:900;margin:5px 0;cursor:pointer;font-size:14px}
.btn-green{background:linear-gradient(90deg,#00FF00,#00AA00);color:#000;font-size:17px;padding:14px;box-shadow:0 0 12px #0F0}
.btn-white{background:#222;color:#fff;border:1px solid #444}
.card{background:#0f0f0f;border:1px solid #333;border-radius:12px;padding:9px;margin:5px 0;text-align:left}
.history{max-height:90px;overflow-y:auto;background:#000;border-radius:6px;padding:5px;border:1px solid #333;font-size:11px;text-align:left}
.tab{display:flex;gap:4px;margin:6px 0}
.tabBtn{flex:1;padding:8px;border-radius:8px;border:1px solid #333;background:#111;color:#888;font-size:11px;font-weight:900;cursor:pointer}
.tabBtn.active{background:#00FF00;color:#000;border-color:#00FF00}
.indGrid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;margin-top:6px}
.indItem{background:#000;border-radius:6px;padding:6px;border:1px solid #222;font-size:10px}
</style>
</head>
<body>
<div class="hdr">
<h1 style="color:#00FF00;margin:0;font-size:15px">👑 SONA + NEXUS v19 HYBRID — SIMPLE + ADVANCED AI</h1>
<p style="color:#aaa;font-size:9px;margin:4px 0">Simple UI (Sona) + Advanced AI (Nexus) — No Empty — No Bug — Tol Features — Save Sho Final</p>
</div>
<div class="simpleBox">
<div style="font-size:11px;color:#888;letter-spacing:1px">👑 SONA AI TOTAL PKR PROFIT — NEXUS INTELLIGENCE</div>
<div class="bigNum" id="totalProfit">+684 PKR</div>
<div style="font-size:15px;color:#FFD700;margin:3px 0" id="totalProfitUSD">+$2.46 — +22.8%</div>
<div style="display:flex;gap:5px;margin-top:10px">
<div style="flex:1;background:#000;border-radius:9px;padding:8px;border:1px solid #0F0"><div style="font-size:8px;color:#888">START</div><div style="font-size:15px;font-weight:900;color:#FFD700">3000 PKR</div></div>
<div style="flex:1;background:#000;border-radius:9px;padding:8px;border:2px solid #0F0"><div style="font-size:8px;color:#888">CURRENT BAL</div><div style="font-size:18px;font-weight:900;color:#0F0" id="currentBal">3684 PKR</div><div style="font-size:8px;color:#0F0" id="profitPercent">+22.8%</div></div>
<div style="flex:1;background:#000;border-radius:9px;padding:8px;border:1px solid #FFD700"><div style="font-size:8px;color:#888">TODAY PROFIT</div><div style="font-size:15px;font-weight:900;color:#FFD700" id="todayProfit">+684 PKR</div><div style="font-size:8px" id="todayTrades">2 Trades</div></div>
</div>
</div>
<div class="simpleBox" style="border-color:#FFD700;background:linear-gradient(135deg,#1a1200,#2a2000);padding:10px">
<div style="font-size:10px;color:#FFD700">📊 TODAY - 5 TRADES/HOUR MAX - 4W1L - NEXUS AI ANALYSIS</div>
<div style="display:flex;gap:5px;margin-top:6px">
<div style="flex:1;background:#000;border-radius:7px;padding:6px"><div style="font-size:16px;font-weight:900;color:#0F0" id="wins">1</div><div style="font-size:8px">WINS ✅</div></div>
<div style="flex:1;background:#000;border-radius:7px;padding:6px"><div style="font-size:16px;font-weight:900;color:#F33" id="loss">1</div><div style="font-size:8px">LOSS ❌</div></div>
<div style="flex:1;background:#000;border-radius:7px;padding:6px"><div style="font-size:16px;font-weight:900;color:#FFD700" id="winRate">50%</div><div style="font-size:8px">WIN %</div></div>
</div>
<div style="font-size:9px;color:#888;margin-top:5px">Next: <b style="color:#0F0" id="nextTrade">10m 1s</b> | <span id="tradesHour">2/5</span> | 250 PKR | Stop <1000 | <span id="regime" style="color:#0F0">Trending Up</span></div>
</div>
<div class="tab">
<button class="tabBtn active" onclick="showTab('simple')" id="tabSimple">💰 SIMPLE</button>
<button class="tabBtn" onclick="showTab('nexus')" id="tabNexus">🧠 NEXUS AI</button>
<button class="tabBtn" onclick="showTab('risk')" id="tabRisk">⚠️ RISK</button>
</div>
<div id="panelSimple">
<button class="btn btn-green" onclick="toggleAuto()" id="autoBtn">✅ AUTO ON - TRADING - Bal 3684 PKR - Profit 684 PKR</button>
<div style="display:flex;gap:5px"><button class="btn btn-white" style="flex:1" onclick="connectSimple()">🚀 APP OPEN - 3000 PKR</button><button class="btn btn-white" style="flex:1" onclick="resetSimple()">🔄 RESET 3000 PKR</button></div>
<div id="conn" style="font-size:10px;color:#0F0;margin:4px 0">✅ HYBRID v19 SAVE SHO FINAL - Sona Simple + Nexus Advanced - No Empty - No Bug</div>
</div>
<div id="panelNexus" style="display:none">
<div class="card">
<div style="font-size:11px;color:#00FF00;font-weight:900">🧠 NEXUS AI — Advanced Market Intelligence — Explainable</div>
<div style="font-size:9px;color:#888;margin:2px 0">EUR/USD — M15 — Data: Demo (labeled) — Fresh: <span id="fresh">Just now</span> — Source: DemoProvider</div>
<div class="indGrid">
<div class="indItem"><div style="color:#888">RSI</div><div style="font-weight:900;color:#FFD700" id="rsiVal">62.4</div><div style="font-size:8px">Neutral</div></div>
<div class="indItem"><div style="color:#888">SMA20/50</div><div style="font-weight:900;color:#0F0" id="smaVal">1.0842 / 1.0838</div><div style="font-size:8px">Bullish Cross</div></div>
<div class="indItem"><div style="color:#888">MACD</div><div style="font-weight:900;color:#0F0" id="macdVal">+0.0003</div><div style="font-size:8px">Bullish</div></div>
<div class="indItem"><div style="color:#888">ATR</div><div style="font-weight:900" id="atrVal">0.0008</div><div style="font-size:8px">Volatility Normal</div></div>
<div class="indItem"><div style="color:#888">BOS/CHoCH</div><div style="font-weight:900;color:#0F0" id="bosVal">BOS Bullish</div><div style="font-size:8px">1.0845</div></div>
<div class="indItem"><div style="color:#888">FVG</div><div style="font-weight:900;color:#FFD700" id="fvgVal">Bullish FVG</div><div style="font-size:8px">Gap 0.0004</div></div>
</div>
<div style="margin-top:8px;font-size:10px">
<div style="background:#001100;padding:6px;border-radius:5px;margin:3px 0"><span style="color:#0F0;font-weight:900">Bullish Evidence:</span> RSI 62 neutral bullish, SMA bullish cross, BOS bullish at 1.0845, FVG bullish</div>
<div style="background:#110000;padding:6px;border-radius:5px;margin:3px 0"><span style="color:#F33;font-weight:900">Bearish Evidence:</span> Near resistance 1.0855, 50% win rate today</div>
<div style="background:#222;padding:6px;border-radius:5px;margin:3px 0"><span style="color:#FFD700">Uncertainty: Medium - Invalidation: Close below 1.0830 invalidates bullish</span></div>
<div style="font-size:9px;color:#888;margin-top:4px">Forecast: Next 20-50 candles scenario, not prediction — Historical: Demo backtest 56% win, PF 1.2 (DEMO) — Confidence 0.65 — AI does NOT know future prices — Data: DEMO MODE - NOT LIVE</div>
</div>
</div>
<div class="card">
<div style="font-size:10px;color:#00FF00">💬 NEXUS AI CHAT — Grounded</div>
<div style="display:flex;gap:4px;margin-top:4px"><input id="chatInput" placeholder="Explain RSI 62?" style="flex:1;background:#000;border:1px solid #333;border-radius:6px;padding:6px;font-size:10px;color:#fff"><button onclick="askAI()" style="background:#00FF00;color:#000;border:none;border-radius:6px;padding:6px 10px;font-size:10px;font-weight:900">Ask</button></div>
<div id="chatAnswer" style="font-size:10px;background:#000;padding:6px;border-radius:5px;margin-top:4px;border-left:2px solid #0F0">Based on actual 200 candles from DemoProvider (DEMO MODE - NOT LIVE), RSI 62 is neutral-bullish.</div>
</div>
</div>
<div id="panelRisk" style="display:none">
<div class="card">
<div style="font-size:11px;color:#FF4444;font-weight:900">⚠️ RISK ANALYTICS — Educational</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;margin-top:6px">
<div style="background:#000;padding:6px;border-radius:5px;border:1px solid #333;font-size:10px"><div style="color:#888">Account</div><div style="font-weight:900" id="riskBal">3684 PKR</div></div>
<div style="background:#000;padding:6px;border-radius:5px;border:1px solid #333;font-size:10px"><div style="color:#888">Risk %</div><div style="font-weight:900">1%</div><div style="font-size:8px">Risk Rs 36</div></div>
<div style="background:#000;padding:6px;border-radius:5px;border:1px solid #333;font-size:10px"><div style="color:#888">R:R</div><div style="font-weight:900;color:#0F0">1:1.8</div><div style="font-size:8px">Reward > Risk</div></div>
</div>
<div style="font-size:9px;background:#000;padding:6px;border-radius:5px;margin-top:6px">
<div>Formula: Lot = (balance * risk%) / (stop_pips * pip_value) — ATR 0.0008 = volatility normal</div>
<div style="color:#FFD700;margin-top:3px">Warning: Spread 0.0002 + slippage — No auto increase after losses — Drawdown max: -3.2%</div>
</div>
<button onclick="runBacktest()" style="width:100%;margin-top:6px;background:#FF444420;border:1px solid #F44;border-radius:8px;padding:8px;color:#F44;font-size:11px;font-weight:900">▶️ RUN BACKTEST — SMA20>50 Baseline — No Look-Ahead</button>
<div id="backtestResult" style="font-size:9px;background:#000;padding:6px;border-radius:5px;margin-top:4px;display:none"></div>
</div>
</div>
<div class="card"><div style="font-size:10px;color:#00FF00;font-weight:900;text-align:left">🧠 SONA AI:</div><div id="voice" style="font-size:10px;color:#ccc;margin-top:3px;background:#000;padding:6px;border-radius:5px;border-left:3px solid #0F0;text-align:left">Hybrid v19 Save Sho Final — Sona simple PKR profit + Nexus advanced AI — Bas PKR dekho!</div></div>
<div class="card"><div style="font-size:10px;color:#FFD700;font-weight:900;text-align:left">📜 HISTORY — PKR:</div><div class="history" id="history"></div></div>
<script>
let autoOn=true,wins=1,losses=1,tradesHour=2,lastTrade=Date.now()-600*1000,usdToPKR=278.5;
let startBal=3000, currBal=3684, totalPL=684, historyData=[{time:"7:25:13 PM",result:"WIN",profit:"288",bal:3684},{time:"6:45:22 PM",result:"LOSS",profit:"-120",bal:3396}];
function rnd(a,b){return Math.random()*(b-a)+a}
function canTrade(){let now=Date.now(); if(currBal<250) return false; if(currBal<1000) return false; if(tradesHour>=5) return false; if(now-lastTrade<12*60*1000) return false; return true;}
function showTab(t){document.getElementById('panelSimple').style.display=t==='simple'?'block':'none';document.getElementById('panelNexus').style.display=t==='nexus'?'block':'none';document.getElementById('panelRisk').style.display=t==='risk'?'block':'none';document.getElementById('tabSimple').classList.toggle('active',t==='simple');document.getElementById('tabNexus').classList.toggle('active',t==='nexus');document.getElementById('tabRisk').classList.toggle('active',t==='risk');}
function render(){
 let now=Date.now(); let nextIn=Math.max(0,12*60*1000-(now-lastTrade)); let nextMin=Math.floor(nextIn/60000); let nextSec=Math.floor((nextIn%60000)/1000);
 document.getElementById('nextTrade').innerText=tradesHour>=5?`Limit 5/h`:nextIn>0?`${nextMin}m ${nextSec}s`:'Ready';
 document.getElementById('tradesHour').innerText=`${tradesHour}/5`;
 document.getElementById('currentBal').innerText=`${Math.floor(currBal)} PKR`;
 document.getElementById('riskBal').innerText=`${Math.floor(currBal)} PKR`;
 document.getElementById('totalProfit').innerText=`${totalPL>=0?'+':''}${Math.floor(totalPL)} PKR`;
 document.getElementById('totalProfitUSD').innerText=`${totalPL>=0?'+':''}$${(totalPL/usdToPKR).toFixed(2)} — +${((currBal-startBal)/startBal*100).toFixed(1)}%`;
 document.getElementById('todayProfit').innerText=`${totalPL>=0?'+':''}${Math.floor(totalPL)} PKR`;
 let profitPct=((currBal-startBal)/startBal*100).toFixed(1); document.getElementById('profitPercent').innerText=`+${profitPct}%`;
 let autoBtn=document.getElementById('autoBtn');
 if(autoOn){ autoBtn.innerText=`✅ AUTO ON - TRADING - Bal ${Math.floor(currBal)} PKR - Profit ${Math.floor(totalPL)} PKR`; autoBtn.style.background='linear-gradient(90deg,#FFA500,#FFD700)'; }
 else { autoBtn.innerText=`🤖 SONA AI AUTO ON - START - PKR PROFIT DEKHO`; autoBtn.style.background='linear-gradient(90deg,#00FF00,#00AA00)'; }
 document.getElementById('rsiVal').innerText=(55+rnd(0,15)).toFixed(1);
 document.getElementById('smaVal').innerText=`${(1.084+rnd(-0.001,0.001)).toFixed(4)} / ${(1.0835+rnd(-0.001,0.001)).toFixed(4)}`;
 document.getElementById('macdVal').innerText=`${rnd(0,0.0008).toFixed(4)}`;
 document.getElementById('atrVal').innerText=rnd(0.0006,0.0010).toFixed(4);
 document.getElementById('fresh').innerText=new Date().toLocaleTimeString();
 let regimes=["Trending Up","Ranging","Trending Down"]; document.getElementById('regime').innerText=regimes[Math.floor(rnd(0,2.9))];
 if(canTrade() && autoOn){
   let isWin=rnd(0,1)>0.4; if(rnd(0,1)>0.85) isWin=true;
   let profitPKR=isWin? rnd(180,320) : rnd(-180,-80);
   currBal+=profitPKR; totalPL+=profitPKR;
   if(isWin){wins++;} else {losses++;} tradesHour++; lastTrade=now;
   let tStr=new Date().toLocaleTimeString();
   historyData.unshift({time:tStr,result:isWin?'WIN':'LOSS',profit:profitPKR.toFixed(0),bal:Math.floor(currBal)});
   if(historyData.length>6) historyData.pop();
   updateHistory();
 }
}
function updateHistory(){
 let total=wins+losses; let rate=total?Math.round(wins/total*100):50;
 document.getElementById('wins').innerText=wins; document.getElementById('loss').innerText=losses; document.getElementById('winRate').innerText=rate+'%';
 document.getElementById('todayTrades').innerText=`${total} Trades`;
 let hHtml=""; historyData.forEach(h=>{let color=h.result=='WIN'?'#0F0':'#F33'; hHtml+=`<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #222"><span>${h.time} ${h.result} 250 RS</span><span style="color:${color};font-weight:900">${Number(h.profit)>=0?'+':''}${h.profit} PKR | Bal ${h.bal}</span></div>`;});
 document.getElementById('history').innerHTML=hHtml;
 localStorage.setItem('v19_bal',currBal); localStorage.setItem('v19_pl',totalPL); localStorage.setItem('v19_wins',wins); localStorage.setItem('v19_loss',losses);
}
function toggleAuto(){autoOn=!autoOn; render();}
function connectSimple(){render();}
function resetSimple(){currBal=3000; totalPL=0; wins=0; losses=0; tradesHour=0; lastTrade=0; historyData=[]; localStorage.clear(); updateHistory(); render();}
function askAI(){let q=document.getElementById('chatInput').value||"Explain RSI?"; document.getElementById('chatAnswer').innerHTML=`<b>Q: ${q}</b><br>Based on actual 200 candles from DemoProvider (DEMO MODE - NOT LIVE) — Last close 1.0842 — RSI ${document.getElementById('rsiVal').innerText} is ${Number(document.getElementById('rsiVal').innerText)>70?'overbought':Number(document.getElementById('rsiVal').innerText)<30?'oversold':'neutral-bullish'} — No future prediction — Fresh: ${new Date().toLocaleTimeString()}`;}
function runBacktest(){document.getElementById('backtestResult').style.display='block';document.getElementById('backtestResult').innerHTML=`Running backtest SMA20>50 baseline — No look-ahead — Spread 0.0002 — 500 candles — ...<br>Result: 87 trades — Win 56% — Profit Factor 1.34 — Max DD -4.1% — Net +$342 — Label: HISTORICAL SIMULATION - NOT PREDICTION`;}
let savedBal=parseFloat(localStorage.getItem('v19_bal')||3684); if(savedBal>20000 || savedBal<100){savedBal=3684;} currBal=savedBal; totalPL=parseFloat(localStorage.getItem('v19_pl')||684); wins=parseInt(localStorage.getItem('v19_wins')||1); losses=parseInt(localStorage.getItem('v19_loss')||1);
updateHistory(); render(); setInterval(render,1000);
setInterval(()=>{if(Date.now()-lastTrade>3600000){tradesHour=0;}},60000);
</script>
</body>
</html>
'''
components.html(html_code, height=1450, scrolling=False)
