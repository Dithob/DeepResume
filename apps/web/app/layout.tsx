import "./globals.css";

export const metadata = {
  title: "CV2Offer Agent",
  description: "CV-JD gap driven learning planner and evidence vault"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
