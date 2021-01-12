module.exports = {
  /////////////////////////////////////////////////////////////////////////
  symbol: ['ETHUSDT', 'BTCUSDT', 'ETHUSDT', 'BTCUSDT', 'ETHUSDT', 'BTCUSDT', 'ETHUSDT', 'BTCUSDT', "ADAUSDT", "ADAUSDT", "ADAUSDT", "ADAUSDT"],
  timeframe: ['1M', '1M', '1w', '1w', '1d', '1d', '8h', '8h', "8h", "1d", "1w", "1M"],
  fromTS:'12/18/2013 12:23:13',//Format - mm/dd/yyyy hh:mm:ss;
  toTS:'12/15/2021 12:23:13',//Format - mm/dd/yyyy hh:mm:ss;
  fileName: ['Data/ETHUSDT_1M_data.csv', 'Data/BTCUSDT_1M_data.csv', 'Data/ETHUSDT_1w_data.csv', 'Data/BTCUSDT_1w_data.csv', 'Data/ETHUSDT_1d_data.csv', 'Data/BTCUSDT_1d_data.csv', 'Data/ETHUSDT_8h_data.csv', 'Data/BTCUSDT_8h_data.csv', 'Data/ADAUSDT_8h_data.csv', 'Data/ADAUSDT_1d_data.csv', 'Data/ADAUSDT_1w_data.csv', 'Data/ADAUSDT_1M_data.csv'],//Export to file name.csv
  ///////////////////////////////////////////////////////////////////////////
  tfw:{
    '1m':1*60*1000,
    '3m':3*60*1000,
    '5m':5*60*1000,
    '15m':15*60*1000,
    '30m':30*60*1000,
    '1h':1*60*60*1000,
    '2h':2*60*60*1000,
    '4h':4*60*60*1000,
    '8h':8*60*60*1000,
    '12h':12*60*60*1000,
    '1d':1*24*60*60*1000,
    '3d':3*24*60*60*1000,
    '1w':7*24*60*60*1000,
    '1M':30*24*60*60*1000,
  },
  getPrameters(){
    return {  symbol:this.symbol,
              timeframe:this.timeframe,
              fromTS:new Date(this.fromTS).getTime(),
              toTS:new Date(this.toTS).getTime(),
              fileName:this.fileName,
              tfw:this.tfw
    };
  }
}