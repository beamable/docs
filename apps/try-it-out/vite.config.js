import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  build: {
    outDir: '../../docs/assets/apps/tryitout', // custom output folder instead of dist/
    lib: {
      entry: 'src/main.js',       // your main entry
      name: 'TryItOutApp',         // the global variable name
      formats: ['iife'],          // could also use 'umd'
    },
    rollupOptions: {
      external: ['beamable-sdk', 'beamable-sdk/api'],
      input: 'src/main.js', // <— point to your JS entry only, NOT index.html
      output: {
        globals: {
          'beamable-sdk': 'Beamable',
          'beamable-sdk/api': 'BeamableApi'
        },
        // JS output
        entryFileNames: 'main.js',
        chunkFileNames: '[name].js', // for code-split chunks
        assetFileNames: (assetInfo) => {
          // Send CSS and other assets to your preferred directories
          if (assetInfo.name && assetInfo.name.endsWith('.css')) {
            return 'main.css' // static name for CSS
          }
          return '[name][extname]'
        },
      },
    },
  },
  plugins: [svelte()],
})
