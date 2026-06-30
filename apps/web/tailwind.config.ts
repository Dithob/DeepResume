import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#18202f",
        paper: "#f7f8f5",
        mint: "#e8f4ef",
        coral: "#e97155",
        cobalt: "#315a9b"
      }
    }
  },
  plugins: []
};

export default config;
