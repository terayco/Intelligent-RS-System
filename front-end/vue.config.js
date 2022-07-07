const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 5008, // 端口
  },
  // transpileDependencies: ['@arcgis']
})

