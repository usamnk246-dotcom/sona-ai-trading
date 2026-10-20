<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sona AI Advance - KING V103 x SONA LINKED</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
body { font-family: 'Inter'; background: #020A14; }
.gold-glow { box-shadow: 0 0 20px rgba(255,215,0,0.15); border: 1px solid rgba(255,215,0,0.3); }
.neon { background: linear-gradient(90deg, #00D4FF, #00FF9D); }
</style>
</head>
<body class="text-white p-4 max-w-[430px] mx-auto">

<!-- Header -->
<div class="flex justify-between items-center">
  <div class="flex items-center gap-3">
    <div class="w-14 h-14 rounded-full bg-gradient-to-br from-yellow-400 to-yellow-600 flex items-center justify-center text-3xl font-black">S</div>
    <div>
      <h1 class="text-3xl font-extrabold">Sona <span class="text-yellow-400">AI</span> <span class="text-xs border border-yellow-400 px-2 py-1 rounded-lg ml-2">ADVANCE</span></h1>
      <p class="text-xs text-gray-400">Smarter Trades • Higher Profits</p>
    </div>
  </div>
  <div class="flex gap-3"><span>🔔<sup class="bg-red-500 rounded-full px-1">3</sup></span><span>👤</span></div>
</div>

<!-- AI Companion -->
<div class="mt-4 rounded-2xl bg-[#081425] p-4 gold-glow relative overflow-hidden">
  <span class="text-xs bg-cyan-900/50 border border-cyan-400 px-3 py-1 rounded-full">⭐ AI Powered Trading</span>
  <h2 class="text-3xl font-bold mt-3 leading-tight">Your <span class="text-cyan-400">AI</span> Trading<br>Companion</h2>
  <p class="text-sm text-gray-400 mt-2">Sona AI analyzes market, finds<br>best opportunities</p>
  <button onclick="startTrading()" class="neon mt-4 px-6 py-3 rounded-full font-bold text-black">📈 Start Trading →</button>
  <div class="absolute right-0 top-0 w-1/2 h-full opacity-80">
    <img src="https://i.imgur.com/8QJ4s2y.png" class="w-full h-full object-cover" style="mask-image: linear-gradient(to left, black, transparent);">
    <!-- Blue AI girl will be from your design -->
    <div class="absolute bottom-0 right-2 text-[10px] text-yellow-400">XAU/USD Gold ↗</div>
  </div>
  <div class="mt-6 text-xs text-yellow-500">• LIVE MARKETS • REAL-TIME</div>
</div>

<!-- Markets -->
<div class="grid grid-cols-4 gap-2 mt-4">
  <div class="bg-[#0B1E35] p-2 rounded-xl"><div class="text-xs">₿ BTC/USDT</div><div class="font-bold">67,432.18</div><div class="text-green-400 text-xs">+2.34% ▲</div></div>
  <div class="bg-[#0B1E35] p-2 rounded-xl"><div class="text-xs">🪙 XAU/USD</div><div class="font-bold">2,658.42</div><div class="text-green-400 text-xs">+0.82% ▲</div></div>
  <div class="bg-[#0B1E35] p-2 rounded-xl"><div class="text-xs">€ EUR/USD</div><div class="font-bold">1.0874</div><div class="text-green-400 text-xs">+0.21% ▲</div></div>
  <div class="bg-[#0B1E35] p-2 rounded-xl"><div class="text-xs">🇬🇧 GBP/USD</div><div class="font-bold">1.2987</div><div class="text-green-400 text-xs">+0.33% ▲</div></div>
</div>

<!-- Automatic Trading + Quality + Win Rate -->
<div class="flex gap-2 mt-3">
  <div class="flex-1 bg-[#0F1F35] rounded-xl p-3 flex justify-between items-center gold-glow">
    <span class="font-bold text-sm">Automatic Trading</span>
    <label class="relative inline-flex items-center cursor-pointer">
      <input type="checkbox" id="autoToggle" checked class="sr-only peer" onchange="toggleAuto()">
      <div class="w-11 h-6 bg-gray-600 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:bg-green-500"></div>
    </label>
  </div>
</div>

<div class="flex gap-2 mt-2 text-[10px]">
  <div class="bg-[#1A2A40] px-3 py-2 rounded-xl border border-yellow-500/30">📊 Quality Filter Score<br>6/7 Minimum</div>
  <div class="bg-[#1A2A40] px-3 py-2 rounded-xl border border-yellow-500">⭐ Win Rate<br>90%</div>
  <div class="bg-[#1A2A40] px-3 py-2 rounded-xl border border-yellow-500">🔗 KING V103 x SONA AI<br>LINKED <span class="bg-green-500 text-[8px] px-1 rounded">Selected</span></div>
</div>

<!-- Features -->
<div class="grid grid-cols-3 gap-3 mt-4">
  <div class="bg-[#0B1E35] p-3 rounded-xl text-center">🎯<br>Signals</div>
  <div class="bg-[#1A1235] p-3 rounded-xl text-center">🧠<br>AI Analysis</div>
  <div class="bg-[#0B1E35] p-3 rounded-xl text-center">⭐<br>Watchlist</div>
</div>

<!-- Market Overview -->
<div class="bg-[#081425] rounded-2xl p-4 mt-4 gold-glow">
  <div class="flex gap-4">
    <div class="flex-1">
      <div class="text-sm text-gray-400">Total Balance 👁️</div>
      <div class="text-3xl font-extrabold">$ 12,452</div>
      <div class="text-green-400 text-sm">+4.32% (24h)</div>
      <div class="mt-2 h-16 bg-gradient-to-t from-cyan-500/30 to-transparent rounded">📈 Chart</div>
    </div>
    <div class="flex-1 space-y-3 text-xs">
      <div class="bg-[#0F2A4A] p-2 rounded-lg">📊 Win Rate 90%<br><b>27W/3L</b></div>
      <div class="bg-[#0F2A2A] p-2 rounded-lg">🎯 Active Trades<br><b>3</b></div>
      <div class="bg-[#2A104A] p-2 rounded-lg">💰 Daily Profit<br><b class="text-green-400">+542.17</b></div>
      <div class="bg-[#0A2A1A] p-2 rounded-lg">🏃 Autotrader Status<br><b id="status" class="text-green-400">Running</b></div>
      <div class="bg-[#2A1F0A] p-2 rounded-lg border border-yellow-500">🔔 Last Alert<br><b>SELL 4185.50 • Quality 6/7</b></div>
    </div>
  </div>
</div>

<!-- Bottom Nav -->
<div class="flex justify-around mt-6 py-3 bg-[#050E1E] rounded-2xl">
  <div class="text-cyan-400">🏠<br>Home</div><div>📊 Markets</div><div>🔄 Trade</div><div>🕒 History</div><div>👤 Profile</div>
</div>

<script>
// KING V103 x SONA AI LINKED - Quality 90% Logic
let qualityScore = 0;
function calculateQuality(data){
  let score=0;
  if(data.ema9 > data.ema21 && data.ema21 > data.ema200) score+=1;
  if(data.close > data.vwap && data.rsi>50) score+=1;
  if(data.rsi>50 && data.macd>data.signal) score+=1;
  if(data.sweep && data.bos) score+=2;
  if(data.ob && data.fvg) score+=1;
  if(data.atr>8 && data.atr<15) score+=1;
  return score;
}

function toggleAuto(){
  const on = document.getElementById('autoToggle').checked;
  document.getElementById('status').innerText = on ? 'Running' : 'Paused';
  if(on) {
    // Example data from your screenshot - 4185.50
    const data = {ema9:4191.9, ema21:4192.8, ema200:4182.9, close:4185.5, vwap:4175.17, rsi:44.5, macd:0.410, signal:0.2, sweep:true, bos:true, ob:true, fvg:true, atr:9.25};
    qualityScore = calculateQuality(data);
    if(qualityScore >=6){
      alert('👑🔔 SELL BAJA! - 4185.50 - Score '+qualityScore+'/7 - KING 103 WAR - Autotrader EXECUTED!');
    } else {
      alert('Low Quality Skipped - Score '+qualityScore+'/7 - Win Rate protect ke liye block kiya!');
    }
  }
}

function startTrading(){
  alert('Sona AI Advance Started! KING V103 x SONA AI LINKED Active! Automatic Trading ON - Win Rate 90% Mode');
  toggleAuto();
}

// Auto check every 30 sec - 30m timeframe
setInterval(()=>{ if(document.getElementById('autoToggle').checked) toggleAuto(); }, 30000);
</script>

</body>
</html>
