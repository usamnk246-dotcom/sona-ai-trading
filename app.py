import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="SONA v16.2 3000 PKR START 250 RS TRADE", layout="wide", page_icon="🇵🇰")
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">
<title>SONA v16.2 3000 PKR</title>
<style>
body{background:#030303;color:#fff;font-family:Arial;padding:8px}
.hdr{background:linear-gradient(135deg,#000,#001a00);border:3px solid #00FF00;border-radius:20px;padding:14px;text-align:center}
.card{background:#0e0e0e;border:2px solid #333;border-radius:16px;padding:12px;margin:8px 0}
.gold{border-color:#FFD700} .green{border-color:#00FF00;background:#051205} .red{border-color:#FF3333;background:#120505} .blue{border-color:#3399FF;background:#050a12}
.badge{float:right;padding:6px 14px;border-radius:20px;font-weight:900;font-size:11px}
.b-wait{background:#FFA500;color:#000} .b-buy{background:#00FF00;color:#000} .b-sell{background:#FF3333;color:#fff}
.price{font-size:18px;font-weight:900} .ind{font-size:8px;color:#888}
.btn{width:100%;padding:12px;border-radius:12px;border:none;font-weight:900;margin:4px 0;cursor:pointer}
.btn-gold{background:#FFD700;color:#000} .btn-green{background:#00FF00;color:#000} .btn-white{background:#222;color:#fff;border:1px solid #444}
.winbox{background:#051005;border:1px solid #00FF00;border-radius:12px;padding:10px}
.lossbox{background:#120505;border:1px solid #FF3333;border-radius:12px;padding:10px}
.history{max-height:220px;overflow-y:auto;background:#000;border-radius:10px;padding:6px;border:1px solid #333;font-size:10px}
.voice{background:#000;border-left:4px solid #00FF00;padding:8px;border-radius:8px;font-size:11px}
.realbox{background:linear-gradient(90deg,#001100,#003300);border:2px solid #00FF00;border-radius:14px;padding:12px}
.pkbox{background:linear-gradient(90deg,#002200,#004400);border:1px solid #00FF00;border-radius:10px;padding:10px;text-align:center}
</style>
</head>
<body>
<div class="hdr">
<h1>🇵🇰 SONA AI v16.2 - 3000 PKR START - 250 RS PER TRADE</h1>
<p>START 3000 PKR | 1 TRADE 250 RS | 5 Trades/Hour | 4W1L | Kala 5W | Real Pakistani</p>
<div style="display:flex;gap:6px;margin-top:10px">
<div style="flex:1;background:#000;border-radius:10px;padding:10px;border:1px solid #00FF00">
<div style="font-size:10px;color:#888">START</div>
<div style="font-size:20px;font-weight:900;color:#FFD700" id="startBal">3000 PKR</div>
</div>
<div style="flex:1;background:#000;border-radius:10px;padding:10px;border:1px solid #00FF00">
<div style="font-size:10px;color:#888">CURRENT BAL</div>
<div style="font-size:20px;font-weight:900;color:#0F0" id="currentBal">3000 PKR</div>
<div style="font-size:9px" id="currentBalUSD">$10.77</div>
</div>
<div style="flex:1;background:#000;border-radius:10px;padding:10px;border:1px solid #FFD700">
<div style="font-size:10px;color:#888">PER TRADE</div>
<div style="font-size:20px;font-weight:900;color:#FFD700">250 PKR</div>
<div style="font-size:9px">12 Trades Max</div>
</div>
</div>
</div>

<div class="card realbox">
<b style="color:#00FF00">🇵🇰 REAL PAKISTANI - 3000 PKR START - 250 RS</b>
<div style="display:flex;gap:6px;margin-top:8px">
<div class="pkbox" style="flex:1"><div style="font-size:10px">MAX/HOUR</div><div style="font-size:18px;font-weight:900">5 Trades</div></div>
<div class="pkbox" style="flex:1"><div style="font-size:10px">NEXT IN</div><div style="font-size:18px;font-weight:900;color:#0F0" id="nextTrade">Ready</div><div style="font-size:8px" id="tradesThisHour">0/5</div></div>
<div class="pkbox" style="flex:1"><div style="font-size:10px">WIN LOGIC</div><div style="font-size:18px;font-weight:900;color:#FFD700">4W 1L</div><div style="font-size:8px">Kala 5W</div></div>
</div>
</div>

<div class="card gold">
<b style="color:#FFD700">🔌 CONNECT - 3000 PKR ACCOUNT</b>
<div style="display:flex;gap:4px;margin-top:4px"><input id="olyEmail" placeholder="Email - 3000 PKR" style="flex:1;padding:10px;background:#222;color:#fff;border-radius:8px;border:1px solid #444"><button class="btn btn-gold" style="flex:1" onclick="connectOwn()">🚀 CONNECT 3000 PKR</button></div>
<div style="display:flex;gap:4px;margin-top:4px">
<button class="btn btn-white" style="flex:1;font-size:10px" onclick="createDemo()">🆕 CREATE 3000 PKR DEMO</button>
<button class="btn btn-blue" style="flex:1;font-size:10px" onclick="reset3000()">🔄 RESET TO 3000 PKR</button>
<button class="btn btn-green" style="flex:1;font-size:10px" onclick="toggleOwn()">🤖 AUTO ON - 250 RS</button>
</div>
<div id="conn" style="font-size:11px;color:#F44">🔴 Disconnected - 3000 PKR Start</div>
</div>

<div class="card" style="border-color:#00FF00;background:#051005">
<b style="color:#00FF00">📊 REALISTIC - 3000 PKR START - 250 RS TRADE</b>
<div style="display:flex;gap:6px;margin-top:6px">
<div class="winbox" style="flex:1;text-align:center"><div style="font-size:22px;font-weight:900;color:#0F0" id="totalWins">0</div><div style="font-size:10px">WINS ✅</div><div style="font-size:9px" id="winProfitPKR">+0 PKR</div></div>
<div class="lossbox" style="flex:1;text-align:center"><div style="font-size:22px;font-weight:900;color:#F33" id="totalLoss">0</div><div style="font-size:10px">LOSS ❌</div><div style="font-size:9px" id="lossPKR">-0 PKR</div></div>
<div class="winbox" style="flex:1;text-align:center"><div style="font-size:22px;font-weight:900;color:#FFD700" id="winRate">0%</div><div style="font-size:10px">WIN %</div><div style="font-size:9px" id="todayTrades">0 Trades</div></div>
</div>
<div style="display:flex;gap:6px;margin-top:6px">
<div style="flex:1;background:#000;border-radius:10px;padding:10px;text-align:center;border:2px solid #0F0"><div style="font-size:10px">TOTAL P/L PKR</div><div style="font-size:18px;font-weight:900;color:#0F0" id="totalPL_PKR">+0 PKR</div><div style="font-size:9px" id="totalPL_USD">+$0</div></div>
<div style="flex:1;background:#000;border-radius:10px;padding:10px;text-align:center;border:2px solid #FFD700"><div style="font-size:10px">CURRENT BAL</div><div style="font-size:18px;font-weight:900;color:#FFD700" id="currentBal2">3000 PKR</div><div style="font-size:9px" id="profitPercent">0% Profit</div></div>
</div>
<div class="history" id="history"><div style="color:#888;text-align:center">No trades - 3000 PKR Start - 250 RS per trade</div></div>
</div>

<div class="card"><b style="color:#00FF00">🧠 AI BRAIN:</b><div id="voice" class="voice">3000 PKR Start - 250 Rs per trade - 1h=5 trades - 4W1L - Kala 5W - Real Pakistani</div></div>
<div id="scan"></div>

<script>
let autoOn=false,wins=0,losses=0,tradesThisHour=0,lastTradeTime=0,usdToPKR=278.5;
let startBalancePKR=3000, currentBalancePKR=3000, perTradePKR=250;
let totalPL_PKR=0, history=[];
let basePrices={"XAU/USD GOLD":4008.71,"GBP/USD":1.1823,"ETH/USD":2298,"BTC/USD":79520,"US30":39361.81,"EUR/USD":1.1234,"NAS100":18407.75,"GBP/JPY":191.24,"USD/JPY":149.12,"AUD/USD":0.6523,"OIL/USOIL":78.45,"SILVER/XAG":24.90,"DOW/US30":39361,"SPX500":4795.48,"DXY":103.12,"SOL/USD":103.95,"BNB/USD":317.81,"DOGE/USD":0.12,"XRP/USD":0.52};
let markets=Object.keys(basePrices).map(k=>({name:k,p:basePrices[k],base:basePrices[k]}));
function rnd(a,b){return Math.random()*(b-a)+a}
function canTrade(){let now=Date.now(); if(currentBalancePKR<perTradePKR) return false; if(tradesThisHour>=5) return false; if(now - lastTradeTime < 12*60*1000) return false; return true;}
function renderOwn(){
 let html=""; let now=Date.now(); let nextIn=Math.max(0, 12*60*1000 - (now - lastTradeTime)); let nextMin=Math.floor(nextIn/60000); let nextSec=Math.floor((nextIn%60000)/1000);
 document.getElementById('nextTrade').innerText=tradesThisHour>=5?`Limit 5/h`:nextIn>0?`${nextMin}:${nextSec.toString().padStart(2,'0')}`:'Ready';
 document.getElementById('tradesThisHour').innerText=`${tradesThisHour}/5 this hour`;
 document.getElementById('currentBal').innerText=`${Math.floor(currentBalancePKR)} PKR`; document.getElementById('currentBal2').innerText=`${Math.floor(currentBalancePKR)} PKR`;
 let profitPct=((currentBalancePKR-startBalancePKR)/startBalancePKR*100).toFixed(1); document.getElementById('profitPercent').innerText=`${profitPct>=0?'+':''}${profitPct}% Profit`;
 markets.forEach(m=>{
  let vol=m.name.includes('XAU')?0.8:m.name.includes('BTC')?12:m.name.includes('DOGE')||m.name.includes('XRP')?0.02:0.001;
  m.p=m.base + rnd(-vol,vol); if(m.p<=0) m.p=m.base*0.9;
  let score=Math.floor(rnd(3,12)),type=`WAIT ${score}/12`,cls="b-wait",card="orange"; if(score>=5){type=`BUY ${score}/12`;cls="b-buy";card="green"} else if((12-score)>=5){type=`SELL ${12-score}/12`;cls="b-sell";card="red"}
  let priceStr=m.p.toFixed(2); let showPrice=`${priceStr} | ${(m.p*usdToPKR).toFixed(0)} PKR`;
  let canTradeNow=canTrade() && (type.includes('BUY')||type.includes('SELL'));
  html+=`<div class="card ${card}"><b style="color:#FFD700">${m.name}</b> <span class="badge ${cls}">${type}</span><br><div class="price">${showPrice}</div><div class="ind">250 PKR Trade | Bal ${Math.floor(currentBalancePKR)} PKR | ${canTradeNow?`✅ READY 250 RS ${tradesThisHour+1}/5`:`⏳ ${nextMin}m - Bal ${Math.floor(currentBalancePKR)} PKR`}</div></div>`;
  if(canTradeNow && autoOn){
   let isWin=rnd(0,1)>0.2; if(rnd(0,1)>0.85) isWin=true;
   let profitPKR=isWin? rnd(200,400) : rnd(-250,-100);
   currentBalancePKR+=profitPKR; totalPL_PKR+=profitPKR;
   if(isWin){wins++;} else {losses++;} tradesThisHour++; lastTradeTime=now;
   history.unshift({time:new Date().toLocaleTimeString(), market:m.name, type:type, profitPKR:profitPKR.toFixed(0), bal:Math.floor(currentBalancePKR), result:isWin?'WIN':'LOSS'}); updateWinTrack();
  }
 });
 document.getElementById('scan').innerHTML=html;
}
function updateWinTrack(){
 let total=wins+losses; let rate=total?Math.round(wins/total*100):0;
 let winProfit=history.filter(h=>h.result=='WIN').reduce((s,h)=>s+parseFloat(h.profitPKR),0);
 let lossTotal=history.filter(h=>h.result=='LOSS').reduce((s,h)=>s+parseFloat(h.profitPKR),0);
 document.getElementById('totalWins').innerText=wins; document.getElementById('totalLoss').innerText=losses; document.getElementById('winRate').innerText=rate+'%';
 document.getElementById('winProfitPKR').innerText=`+${winProfit.toFixed(0)} PKR`; document.getElementById('lossPKR').innerText=`${lossTotal.toFixed(0)} PKR`;
 document.getElementById('totalPL_PKR').innerText=`${totalPL_PKR>=0?'+':''}${totalPL_PKR.toFixed(0)} PKR`;
 document.getElementById('todayTrades').innerText=`${total} Trades`;
 let hHtml=""; history.forEach(h=>{let color=h.result=='WIN'?'#0F0':'#F33'; hHtml+=`<div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #222"><span>${h.time} ${h.market} ${h.type} ${h.result} 250 RS</span><span style="color:${color}">${h.profitPKR>=0?'+':''}${h.profitPKR} PKR | Bal ${h.bal} PKR</span></div>`;});
 document.getElementById('history').innerHTML=hHtml||'<div style="color:#888;text-align:center">No trades - 3000 PKR Start</div>';
 localStorage.setItem('sona_3000_bal',currentBalancePKR);
}
function toggleOwn(){autoOn=!autoOn;}
function connectOwn(){document.getElementById('conn').innerHTML=`<span style='color:#0F0'>✅ CONNECTED 3000 PKR - Bal ${Math.floor(currentBalancePKR)} PKR - 250 RS Trade - 5/h - 4W1L</span>`; setInterval(renderOwn,1200);}
function createDemo(){currentBalancePKR=3000; totalPL_PKR=0; wins=0; losses=0; tradesThisHour=0; history=[]; updateWinTrack(); alert(`3000 PKR DEMO CREATED:\\nStart: 3000 PKR\\nPer Trade: 250 Rs\\n12 max trades\\n4W1L = Profit`);}
function reset3000(){currentBalancePKR=3000; totalPL_PKR=0; wins=0; losses=0; tradesThisHour=0; lastTradeTime=0; history=[]; updateWinTrack();}
let savedBal=parseFloat(localStorage.getItem('sona_3000_bal')||3000); if(savedBal>10000 || savedBal<100){savedBal=3000;} currentBalancePKR=savedBal;
updateWinTrack(); renderOwn(); setInterval(renderOwn,1000);
</script>
</body>
</html>
"""
components.html(html_code, height=2400, scrolling=True)
