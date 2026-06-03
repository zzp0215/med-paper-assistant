import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "医学论文智能助手",
  description: "基于 RAG 的医学综述写作助手",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
