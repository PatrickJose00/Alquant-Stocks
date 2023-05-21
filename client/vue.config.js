const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === "production" ? "/" : "/",
  devServer: {
    headers: { "Access-Control-Allow-Origin": "*" },
    proxy: {
      '/stocks': {
        target: 'http://localhost:8000',
        pathRewrite: { '^/stocks': '' },
        changeOrigin: true
      },
    }
}
})
