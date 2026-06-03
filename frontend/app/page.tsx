export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-white to-slate-50">
      <div className="container mx-auto px-6 py-16">
        <header className="mb-12">
          <h1 className="text-4xl font-bold text-slate-900">
            医学论文智能助手
          </h1>
          <p className="mt-3 text-lg text-slate-600">
            上传 PDF,自动生成中文医学综述初稿
          </p>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
            <div className="text-2xl">📤</div>
            <h2 className="mt-3 text-lg font-semibold">1. 上传 PDF</h2>
            <p className="mt-2 text-sm text-slate-600">
              支持批量上传英文医学论文 PDF
            </p>
          </div>

          <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
            <div className="text-2xl">💬</div>
            <h2 className="mt-3 text-lg font-semibold">2. 对话澄清</h2>
            <p className="mt-2 text-sm text-slate-600">
              输入标题或与 AI 对话,确定论文方向
            </p>
          </div>

          <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
            <div className="text-2xl">📝</div>
            <h2 className="mt-3 text-lg font-semibold">3. 生成初稿</h2>
            <p className="mt-2 text-sm text-slate-600">
              自动检索参考库,生成带引用的中文初稿
            </p>
          </div>
        </section>

        <section className="mt-12 rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
          <h2 className="text-lg font-semibold">系统状态</h2>
          <p className="mt-2 text-sm text-slate-500">
            当前为 P0 骨架阶段,后续将逐步接入:
            PDF 解析 → 检索 → 大纲生成 → 章节写作 → 改稿 → 引用补全
          </p>
        </section>
      </div>
    </main>
  );
}
