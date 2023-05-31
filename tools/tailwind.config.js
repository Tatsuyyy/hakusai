module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: false,
    content: ['../**/templates/*.html', '../**/templates/**/*.html'],
  },
  theme: {
    extend: {
        spacing:{
          '1/6': '16.6666667%',
          '2/6': '33.3333333%',
          '3/6': '50%',
          '4/6': '66.6666667%',
          '5/6': '83.3333333%',
        }
      }
    },
    variants: {},
  plugins: [],
}