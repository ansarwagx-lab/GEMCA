/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        royal: '#0B2A6B',
        'royal-deep': '#05143a',
        'royal-light': '#2E5BC7',
        platinum: '#C9D0DB',
        'platinum-dp': '#AEB6C2',
        gold: '#C7A663',
        'gold-light': '#E9D4A0',
        'gold-deep': '#A9823F',
        ink: '#11141A',
        paper: '#FFFFFF',
        mist: '#F5F6F9',
        line: '#E7E9EF',
        muted: '#828A99',
      },
      fontFamily: {
        display: ['Jost', 'sans-serif'],
        body: ['Archivo', 'sans-serif'],
      },
      letterSpacing: {
        widest2: '0.2em',
        widest3: '0.22em',
      },
      backgroundImage: {
        'gradient-royal': 'linear-gradient(135deg, #05143a 0%, #0B2A6B 50%, #2E5BC7 100%)',
        'gradient-mesh': 'radial-gradient(at 30% 20%, #2E5BC720 0, transparent 60%), radial-gradient(at 70% 80%, #0B2A6B40 0, transparent 50%), radial-gradient(at 90% 10%, #C7A66310 0, transparent 40%)',
      },
      backdropBlur: {
        xs: '2px',
      },
      boxShadow: {
        glass: '0 8px 32px 0 rgba(5, 20, 58, 0.24), inset 0 1px 0 rgba(255,255,255,0.12)',
        'glass-lg': '0 24px 64px 0 rgba(5, 20, 58, 0.32), inset 0 1px 0 rgba(255,255,255,0.16)',
        gold: '0 0 0 1px rgba(199,166,99,0.3)',
      },
      animation: {
        'drift': 'drift 8s ease-in-out infinite',
        'sheen': 'sheen 0.6s ease forwards',
        'fade-up': 'fadeUp 0.7s ease forwards',
        'counter': 'counter 2s ease-out forwards',
      },
      keyframes: {
        drift: {
          '0%, 100%': { transform: 'translateY(0px) rotate(0deg)' },
          '33%': { transform: 'translateY(-10px) rotate(0.5deg)' },
          '66%': { transform: 'translateY(6px) rotate(-0.3deg)' },
        },
        fadeUp: {
          from: { opacity: '0', transform: 'translateY(24px)' },
          to: { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
};
