const path = require('path');
const webpack = require('webpack')

module.exports = {
  mode: "development",
  entry: {
    main: path.resolve(__dirname, 'src/index.js')  
  },
  output: {
    path: path.resolve(__dirname, '../static/js/'),
    filename: '[name].js',
  },
  module: {
      rules: [
          {
            test: /\.js$/,
            exclude: /node_modules/,
            use: 'babel-loader',
          }
      ]
  },
  resolve: {
      extensions: ['*', '.js', '.jsx'],
      modules: [
          path.resolve(__dirname, 'src'),
          path.resolve(__dirname, 'node_modules'),
      ]
  },
  plugins: [
    //
  ],
}