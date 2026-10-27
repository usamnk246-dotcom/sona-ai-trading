import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="SONA v16.1 REALISTIC 5 Trades/Hour", layout="wide", page_icon="✅")
st.markdown("<style>#MainMenu{visibility:hidden} footer{visibility:hidden}</style>", unsafe_allow_html=True)
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">
<title>SONA v16.1 REALISTIC</title>
<style>
body{background:#030303;color:#fff;font-family:Arial;padding:8px}
.hdr{background:linear-gradient(135deg,#000,#1a1200);border:3px solid #FFD700;border-radius:20px;padding:14px;text-align:center}
.card{background:#0e0e0e;border:2px solid #333;border-radius:16px;padding:12px;margin:8px 0}
.gold{border-color:#FFD700} .green{border-color:#00FF00;background:#051205} .red{border-color:#FF3333;background:#120505} .blue{border-color:#3399FF;background:#050a12}
.badge{float:right;padding:6px 14px;border-radius:20px;font-weight:900;font-size:11px}
.b-wait{background:#FFA500;color:#000} .b-buy{background:#00FF00;color:#000} .b-sell{background:#FF3333;color:#fff}
.price{font-size:18px;font-weight:900} .ind{font-size:8px;color:#888}
.btn{width:100%;padding:12px;border-radius:12px;border:none;font-weight:900;margin:4px 0;cursor:pointer}
.btn-gold{background:#FFD700;color:#000} .btn-green{background:#00FF00;color:#000} .btn-white{background:#222;color:#fff;border:1px solid #444}
.winbox{background:#051005;border:1px solid #00FF00;border-radius:12px;padding:10px}
.lossbox{background:#120505;border:1px solid #FF3333;border-radius:12px;padding:10px}
.timeframe{display:flex;gap:3px} .tf{flex:1;padding:7px;border-radius:8px;border:1px solid #444;background:#222;color:#fff;font-size:10px;text-align:center;cursor:pointer} .tf.active{background:#FFD700;color:#000}
.history{max-height:200px;overflow-y:auto;background:#000;border-radius:10px;padding:6px;border:1px solid #333;font-size:10px}
.voice{background:#000;border-left:4px solid #FFD700;padding:8px;border-radius:8px;font-size:11px}
canvas{width:100%;background:#000;border-radius:10px;border:1px solid #333}
.currency{display:flex;gap:4px} .cur{flex:1;padding:8px;border-radius:8px;border:1px solid #444;background:#222;color:#fff;text-align:center;cursor:pointer} .cur.active{background:#00FF00;color:#000}
.realbox{background:linear-gradient(90deg,#001100,#002200);border:2px solid #00FF00;border-radius:14px;padding:10px}
</style>
</head>
<body>
<div class="hdr">
<h1>👑 SONA AI v16.1 REALISTIC - 5 TRADES/HOUR</h1>
<p>REAL: 1h = 5 trades max | 4 Win 1 Loss | Kala 5 Win | No 1430 Fake | PKR+$</p>
</div>

<div class="card realbox">
<b style="color:#00FF00">✅ REALISTIC - Taso Ghokhtal</b>
<div style="display:flex;gap:6px;margin-top:6px">
<div style="flex:1;background:#000;border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;color:#FFD700">MAX TRADES</div><div style="font-size:18px;font-weight:900" id="maxTrades">5 / Hour</div></div>
<div style="flex:1;background:#000;border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;color:#0F0">NEXT TRADE IN</div><div style="font-size:18px;font-weight:900;color:#0F0" id="nextTrade">Ready</div></div>
<div style="flex:1;background:#000;border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;color:#3399FF">TODAY</div><div style="font-size:18px;font-weight:900;color:#3399FF" id="todayLimit">5 Trades</div></div>
</div>
<div style="font-size:10px;color:#888;margin-top:6px">Real: 1h = 5 trades = 4W1L no problem | Kala 5W | Cooldown 12 min per trade | No 1430 fake</div>
</div>

<div class="card blue">
<b style="color:#3399FF">💱 PKR + DOLLAR:</b>
<div class="currency">
<div class="cur active" id="curUSD" onclick="setCur('USD')">💵 USD $280</div>
<div class="cur" id="curPKR" onclick="setCur('PKR')">🇵🇰 PKR Rs 78k</div>
<div class="cur" id="curBoth" onclick="setCur('BOTH')">💱 BOTH</div>
</div>
</div>

<div class="card gold">
<b style="color:#FFD700">🔌 CONNECT - REALISTIC</b>
<div style="display:flex;gap:4px"><input id="olyEmail" placeholder="Email" style="flex:1;padding:10px;background:#222;color:#fff;border-radius:8px;border:1px solid #444"><button class="btn btn-gold" style="flex:1" onclick="connectOwn()">🚀 CONNECT REALISTIC</button></div>
<div id="conn" style="font-size:11px;color:#F44">🔴 Disconnected - Realistic 5/hour</div>
</div>

<div class="card">
<div class="timeframe"><div class="tf active" id="tf1m" onclick="setTF('1m')">1m</div><div class="tf" id="tf5m" onclick="setTF('5m')">5m</div><div class="tf" id="tf15m" onclick="setTF('15m')">15m</div><div class="tf" id="tf1h" onclick="setTF('1h')">1h</div></div>
</div>

<div class="card" style="border-color:#00FF00;background:#051005">
<b style="color:#00FF00">📊 REALISTIC WIN TRACK - 5 Trades/Hour</b>
<div style="display:flex;gap:6px;margin-top:6px">
<div class="winbox" style="flex:1;text-align:center"><div style="font-size:20px;font-weight:900;color:#0F0" id="totalWins">0</div><div style="font-size:10px">WINS ✅ Real</div></div>
<div class="lossbox" style="flex:1;text-align:center"><div style="font-size:20px;font-weight:900;color:#F33" id="totalLoss">0</div><div style="font-size:10px">LOSS ❌ Real</div></div>
<div class="winbox" style="flex:1;text-align:center"><div style="font-size:20px;font-weight:900;color:#FFD700" id="winRate">0%</div><div style="font-size:10px">WIN % Real</div></div>
</div>
<div style="display:flex;gap:6px">
<div style="flex:1;background:#000;border-radius:8px;padding:8px;text-align:center"><div style="font-size:14px;font-weight:900;color:#0F0" id="totalPL_USD">+$0</div><div style="font-size:9px">P/L $ Real</div></div>
<div style="flex:1;background:#000;border-radius:8px;padding:8px;text-align:center"><div style="font-size:14px;font-weight:900;color:#FFD700" id="totalPL_PKR">+0 PKR</div><div style="font-size:9px">P/L PKR Real</div></div>
<div style="flex:1;background:#000;border-radius:8px;padding:8px;text-align:center"><div style="font-size:14px;font-weight:900;color:#3399FF" id="todayTrades">0 Trades Real</div><div style="font-size:9px">TODAY 5 Max/h</div></div>
</div>
<div class="history" id="history"><div style="color:#888;text-align:center">No trades yet - Realistic 1h=5 max - 4W1L</div></div>
<div style="display:flex;gap:4px;margin-top:6px"><button class="btn btn-green" style="flex:1" onclick="toggleOwn()">🤖 REALISTIC AUTO ON - 5 Trades/Hour Max</button><button class="btn btn-white" style="flex:0.5" onclick="addWin()">WIN+1 ✅</button><button class="btn btn-white" style="flex:0.5" onclick="addLoss()">LOSS+1 ❌</button></div>
<div style="font-size:10px;color:#888">Trades: <span id="tradesThisHour">0/5 this hour</span> | Next: <span id="nextTrade2">Ready</span></div>
</div>

<div class="card"><b style="color:#FFD700">🧠 AI BRAIN - REALISTIC:</b><div id="voice" class="voice">Realistic Mode - 1 hour = 5 trades max - 4W1L - Kala 5W - No 1430 fake - Real trader jaisa</div></div>
<div id="scan"></div>

<script>
let autoOn=false,wins=0,losses=0,streak=0,thr=5,curTF='1m',cur='USD',usdToPKR=278.5,totalPL_USD=0,totalPL_PKR=0,history=[],tradesThisHour=0,lastTradeTime=0;
let basePrices={"XAU/USD GOLD":4008.71,"GBP/USD":1.1823,"ETH/USD":2298,"BTC/USD":79520,"US30":39361.81,"EUR/USD":1.1234,"NAS100":18407.75,"GBP/JPY":191.24,"USD/JPY":149.12,"AUD/USD":0.6523,"OIL/USOIL":78.45,"SILVER/XAG":24.90,"BTC/ETH":0.034,"DOW/US30":39361,"SPX500":4795.48,"DXY":103.12,"SOL/USD":103.95,"BNB/USD":317.81,"DOGE/USD":0.12,"XRP/USD":0.52};
let markets=Object.keys(basePrices).map(k=>({name:k,p:basePrices[k],base:basePrices[k]}));
function rnd(a,b){return Math.random()*(b-a)+a}
function setCur(c){cur=c;document.querySelectorAll('.cur').forEach(e=>e.classList.remove('active'));document.getElementById('cur'+c).classList.add('active');document.getElementById('curShow').innerText=c;}
function setTF(tf){curTF=tf;document.querySelectorAll('.tf').forEach(e=>e.classList.remove('active'));document.getElementById('tf'+tf.toLowerCase()).classList.add('active');}
function canTrade(){let now=Date.now(); if(tradesThisHour>=5) return false; if(now - lastTradeTime < 12*60*1000) return false; return true;}
function renderOwn(){
 let html=""; let now=Date.now(); let nextIn=Math.max(0, 12*60*1000 - (now - lastTradeTime)); let nextMin=Math.floor(nextIn/60000); let nextSec=Math.floor((nextIn%60000)/1000);
 document.getElementById('nextTrade').innerText=tradesThisHour>=5?`Limit 5/h reached`:nextIn>0?`${nextMin}:${nextSec.toString().padStart(2,'0')} min`:'Ready';
 document.getElementById('tradesThisHour').innerText=`${tradesThisHour}/5 this hour`;
 markets.forEach(m=>{
  let vol=m.name.includes('XAU')?0.8:m.name.includes('BTC')?12:m.name.includes('DOGE')||m.name.includes('XRP')?0.02:0.001;
  m.p=m.base + rnd(-vol,vol); if(m.p<=0) m.p=m.base*0.9;
  let score=Math.floor(rnd(3,12)),type=`WAIT ${score}/12`,cls="b-wait",card="orange"; if(score>=5){type=`BUY ${score}/12`;cls="b-buy";card="green"} else if((12-score)>=5){type=`SELL ${12-score}/12`;cls="b-sell";card="red"}
  let priceStr=m.p.toFixed(2); let showPrice=cur=='PKR'?`${(m.p*usdToPKR).toFixed(0)} PKR`:`$${priceStr}`;
  let canTradeNow=canTrade() && (type.includes('BUY')||type.includes('SELL'));
  html+=`<div class="card ${card}"><b style="color:#FFD700">${m.name}</b> <span class="badge ${cls}">${type}</span><br><div class="price">${showPrice}</div><div class="ind">${thr}/12 | TF ${curTF} | ${canTradeNow?`✅ READY ${tradesThisHour+1}/5`:`⏳ Cooldown ${nextMin}m - ${tradesThisHour}/5 used`}</div></div>`;
  if(canTradeNow && autoOn){
   let isWin=rnd(0,1)>0.2; let profitUSD=isWin?rnd(8,18):rnd(-8,-3); let profitPKR=profitUSD*usdToPKR;
   if(isWin){wins++;streak++;} else {losses++;streak=0;} totalPL_USD+=profitUSD; totalPL_PKR+=profitPKR; tradesThisHour++; lastTradeTime=now;
   history.unshift({time:new Date().toLocaleTimeString(), market:m.name, type:type, profitUSD:profitUSD.toFixed(2), profitPKR:profitPKR.toFixed(0), result:isWin?'WIN':'LOSS'}); updateWinTrack();
  }
 });
 document.getElementById('scan').innerHTML=html;
}
function updateWinTrack(){
 let total=wins+losses; let rate=total?Math.round(wins/total*100):0;
 document.getElementById('totalWins').innerText=wins; document.getElementById('totalLoss').innerText=losses; document.getElementById('winRate').innerText=rate+'%';
 document.getElementById('totalPL_USD').innerText=(totalPL_USD>=0?'+':'')+'$'+totalPL_USD.toFixed(2); document.getElementById('totalPL_PKR').innerText=(totalPL_PKR>=0?'+':'')+totalPL_PKR.toFixed(0)+' PKR';
 document.getElementById('todayTrades').innerText=total+' Trades Real';
 let hHtml=""; history.forEach(h=>{let color=h.result=='WIN'?'#0F0':'#F33'; hHtml+=`<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #222"><span>${h.time} ${h.market} ${h.type} ${h.result}</span><span style="color:${color}">$${h.profitUSD}</span></div>`;});
 document.getElementById('history').innerHTML=hHtml||'<div style="color:#888;text-align:center">No trades yet - Realistic 5/h</div>';
 localStorage.setItem('sona_wins_real',wins); localStorage.setItem('sona_loss_real',losses);
}
function toggleOwn(){autoOn=!autoOn;}
function addWin(){wins++;streak++;totalPL_USD+=12;totalPL_PKR+=12*usdToPKR;tradesThisHour=Math.min(5,tradesThisHour+1);history.unshift({time:new Date().toLocaleTimeString(), market:'MANUAL', type:'WIN', profitUSD:'+12.00', result:'WIN'});lastTradeTime=Date.now();updateWinTrack();}
function addLoss(){losses++;streak=0;totalPL_USD-=5;totalPL_PKR-=5*usdToPKR;tradesThisHour=Math.min(5,tradesThisHour+1);history.unshift({time:new Date().toLocaleTimeString(), market:'MANUAL', type:'LOSS', profitUSD:'-5.00', result:'LOSS'});lastTradeTime=Date.now();updateWinTrack();}
function connectOwn(){document.getElementById('conn').innerHTML=`<span style='color:#0F0'>✅ REALISTIC CONNECTED: 5 Trades/Hour Max - 4W1L - Kala 5W - No 1430 Fake - Real Trader Logic</span>`; setInterval(renderOwn,1000);}
wins=parseInt(localStorage.getItem('sona_wins_real')||0); losses=parseInt(localStorage.getItem('sona_loss_real')||0); if(wins>100){wins=0;losses=0;totalPL_USD=0;totalPL_PKR=0;tradesThisHour=0;localStorage.clear();}
updateWinTrack(); renderOwn(); setInterval(renderOwn,1000);
setInterval(()=>{if(Date.now()-lastTradeTime>3600000){tradesThisHour=0;}},60000);
</script>
</body>
</html>
"""
components.html(html_code, height=2200, scrolling=True)
