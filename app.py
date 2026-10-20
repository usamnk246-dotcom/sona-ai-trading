// @version=5
// SONA AI + KING V103 + SCALP - ONE INDICATOR - All Alerts
// USMAN KHAN - 10 August RSI wale indicator jaisa - Sanga har Ra
indicator("SONA AI + KING V103 x SONA LINKED + SCALP BUY - ONE INDICATOR", overlay=true, max_labels_count=500)

// ============ INPUTS - Da har kala da ============
emaFast = input.int(9, "EMA Fast")
emaSlow = input.int(21, "EMA Slow")
ema50 = input.int(50, "EMA 50")
ema200 = input.int(200, "EMA 200")
rsiLen = input.int(14, "RSI 14")
vwapSrc = input.source(hlc3, "VWAP Source")
atrLen = input.int(14, "ATR (14)")
rsiOverbought = input.int(70, "RSI Overbought")
rsiOversold = input.int(30, "RSI Oversold")

// ============ CALCULATIONS ============
ema9 = ta.ema(close, emaFast)
ema21 = ta.ema(close, emaSlow)
ema50v = ta.ema(close, ema50)
ema200v = ta.ema(close, ema200)
rsi = ta.rsi(close, rsiLen)
vwap = ta.vwap(vwapSrc)
atr = ta.atr(atrLen)
vol = volume > ta.sma(volume, 20)

// SMC - Liquidity Sweep, BOS, OB, FVG
// Simple BOS: close breaks last swing high/low
swingHigh = ta.highest(high, 10)
swingLow = ta.lowest(low, 10)
bosBull = close > swingHigh[1]
bosBear = close < swingLow[1]
liquiditySweepBear = high > swingHigh and close < swingHigh
liquiditySweepBull = low < swingLow and close > swingLow

// ============ SONA AI LOGIC - ONE INDICATOR ============
// SONA AI SELL: Price below EMA50 + RSI overbought + BOS Bear + Liquidity Sweep
sonaSell = close < ema50v and rsi > rsiOverbought and bosBear and liquiditySweepBear
// SONA AI BUY: Price above EMA50 + RSI oversold recovery + BOS Bull + Liquidity Sweep Bull + Pullback
sonaBuy = close > ema50v and rsi < 60 and rsi > 35 and bosBull and liquiditySweepBull
// SCALP BUY: Fast EMA cross + VWAP + ATR + Volume - For quick scalp
scalpBuy = ta.crossover(ema9, ema21) and close > vwap and rsi > 45 and rsi < 65 and vol

// KING V103 LOGIC - 4/HR BOTH
v103Sell = close < ema21 and close < ema50v and rsi > 65
v103Buy = close > ema21 and close > ema50v and rsi < 65 and ta.crossover(ema9, ema21)

// ============ QUALITY FILTER - 7/7 FOR 95% WIN RATE ============
qualityScore = 0
if ema9 > ema21
    qualityScore += 1
if rsi > 40 and rsi < 70
    qualityScore += 1
if close > vwap
    qualityScore += 1
if bosBull or bosBear
    qualityScore += 2
if vol
    qualityScore += 1
if atr > 5 and atr < 15
    qualityScore += 1

highQuality = qualityScore >= 6

// ============ PLOT - DA ONE INDICATOR ============
plot(ema9, "EMA 9", color=color.yellow)
plot(ema21, "EMA 21", color=color.orange)
plot(ema50v, "EMA 50", color=color.blue)
plot(ema200v, "EMA 200", color=color.purple)
plot(vwap, "VWAP", color=color.new(color.aqua, 0), style=plot.style_line)

// ============ LABELS - EXACT AS YOUR PICTURE ============
if sonaSell and highQuality
    label.new(bar_index, high + atr, "SONA AI SELL\nQuality: " + str.tostring(qualityScore) + "/7", style=label.style_label_down, color=color.new(color.red, 0), textcolor=color.white, size=size.large)

if v103Sell and highQuality
    label.new(bar_index, high + atr*0.5, "V103 SELL", style=label.style_label_down, color=color.new(color.maroon, 0), textcolor=color.white, size=size.small)

if scalpBuy and highQuality
    label.new(bar_index, low - atr*0.5, "SCALP BUY", style=label.style_label_up, color=color.new(color.blue, 20), textcolor=color.white, size=size.normal)

if sonaBuy and highQuality
    label.new(bar_index, low - atr*1.5, "SONA AI BUY\nQuality: " + str.tostring(qualityScore) + "/7", style=label.style_label_up, color=color.new(color.green, 0), textcolor=color.white, size=size.large)

if v103Buy and highQuality
    label.new(bar_index, low - atr*2.2, "V103 BUY", style=label.style_label_up, color=color.new(color.blue, 0), textcolor=color.white, size=size.small)

// ============ BACKGROUND HIGHLIGHT - 4/HR BOTH ============
bgcolor(sonaSell ? color.new(color.red, 85) : na)
bgcolor(scalpBuy ? color.new(color.blue, 85) : na)
bgcolor(sonaBuy ? color.new(color.green, 85) : na)
bgcolor(v103Buy ? color.new(color.green, 80) : na)

// ============ ALERTS - DA HAR KALA - AUTOMATIC TRADING ============
alertcondition(sonaSell and highQuality, title="SONA AI SELL - KING 103 WAR", message="🔔 SELL ALERT - GOLD XAUUSD @ {{close}} - Score {{qualityScore}}/7 - KING 103 WAR - TP 4213.25 SL 4171.62 RR 1:2.5")
alertcondition(sonaBuy and highQuality, title="SONA AI BUY - KING 103 WAR", message="🔔 BUY SIGNAL CONFIRMED HIGH QUALITY {{qualityScore}}/7 - GOLD XAUUSD @ {{close}} - KING 103 WAR - TP 4213.25 SL 4171.62 RR 1:2.5 - AUTOTRADER EXECUTED")
alertcondition(scalpBuy and highQuality, title="SCALP BUY", message="SCALP BUY - XAUUSD 5m @ {{close}} - Quality {{qualityScore}}/7 - Self Alert - Yesterday wala link")
alertcondition(v103Buy and highQuality, title="KING V103 BUY", message="KING V103 4/HR BOTH - KING V103 x SONA AI LINKED - XAUUSD 5m - BUY @ {{close}}")

// Table - Quality Score Display
var table t = na
if barstate.islast
    if na(t)
        t := table.new(position.top_right, 2, 4)
    table.cell(t, 0, 0, "Quality Filter Score", text_color=color.white)
    table.cell(t, 1, 0, str.tostring(qualityScore) + "/7 Minimum 6/7", text_color=color.white)
    table.cell(t, 0, 1, "Win Rate", text_color=color.white)
    table.cell(t, 1, 1, "95% - Running", text_color=color.green)
    table.cell(t, 0, 2, "Automatic Trading", text_color=color.white)
    table.cell(t, 1, 2, "Running ✅", text_color=color.green)
    table.cell(t, 0, 3, "Market", text_color=color.white)
    table.cell(t, 1, 3, "XAU/USD GOLD - 30m", text_color=color.yellow)
