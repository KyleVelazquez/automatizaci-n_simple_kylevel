import yfinance as yf

def obtener_precio_accion(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.history(period="1d")
    precio_actual = info['Close'].iloc[-1]
    return f"El precio actual de {symbol} es ${precio_actual:.2f}"
