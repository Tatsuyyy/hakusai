module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  content: ['./**/templates/*.html', './**/templates/**/*.html'],
  theme: {
    extend: {
        spacing:{
          '1/5': '20%',
          '2/5': '40%',
          '3/5': '60%',
          '4/5': '80%',
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