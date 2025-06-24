# Binance Futures Testnet Trading Bot (USDT-M)

A lightweight command-line trading bot for the Binance Futures **Testnet**.  
Supports placing **Market**, **Limit**, and **Stop-Limit** orders for both **BUY** and **SELL** sides.

---

##  Features

- Place **Market Orders** (Buy/Sell)
- Place **Limit Orders** (Buy/Sell)
- Place **Stop-Limit Orders** (Buy/Sell)
- View open orders
- Check USDT balance
- Error handling and logging
- Interactive CLI interface
- Uses official `binance` Python SDK
  Runs on Binance **Futures Testnet**

---

##  Setup Instructions

### 1. Clone the repository
     git clone https://github.com/YOUR_USERNAME/futures-trading-bot.git
     cd futures-trading-bot
2. Create virtual environment

       python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate
API Key Setup
 Create a Binance Futures Testnet account:
 https://testnet.binancefuture.com

 Generate API keys and enable TRADE, USER_DATA permissions.

 Create a .env file:
          
    API_KEY=your_testnet_api_key
    API_SECRET=your_testnet_api_secret

 Run the Bot

    python chatbot.py

Then follow the CLI prompts:
    
    === Binance Futures Testnet Trading Bot ===
    1. Check Balance
    2. Place Market Order
    3. Place Stop-Limit Order
    4. Place Limit Order
    5. Get Open Orders
    6. Exit
Project Structure

    ├── main.py              
    ├── requirements.txt     
    ├── .env                 
    ├── .gitignore           
    └── trading_bot.log      

    
