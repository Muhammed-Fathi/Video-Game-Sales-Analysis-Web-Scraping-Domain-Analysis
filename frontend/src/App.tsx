import { useState, useEffect } from "react";
import {
  Gamepad2,
  BookOpen,
  FileCode2,
  Terminal,
  ChevronDown,
  ExternalLink,
  BarChart3,
  Database,
  Globe,
  Sparkles,
  CheckCircle2,
  ArrowRight,
  Menu,
  X,
  Cpu,
} from "lucide-react";

/* ───────────────────────────────── NAVBAR ───────────────────────────────── */

function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const links = [
    { label: "Overview", href: "#overview" },
    { label: "Task 1", href: "#task1" },
    { label: "Task 2", href: "#task2" },
    { label: "Task 3", href: "#task3" },
    { label: "Files", href: "#files" },
    { label: "Setup", href: "#setup" },
    { label: "Tech Stack", href: "#tech" },
  ];

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled
          ? "bg-slate-900/95 backdrop-blur-md shadow-lg shadow-slate-900/20"
          : "bg-transparent"
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <a href="#" className="flex items-center gap-2 text-white font-bold text-lg">
            <BarChart3 className="w-6 h-6 text-indigo-400" />
            <span>DS Project</span>
          </a>
          <div className="hidden md:flex items-center gap-6">
            {links.map((l) => (
              <a key={l.href} href={l.href} className="text-slate-300 hover:text-white text-sm font-medium transition-colors">
                {l.label}
              </a>
            ))}
          </div>
          <button className="md:hidden text-slate-300" onClick={() => setMenuOpen(!menuOpen)}>
            {menuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
        {menuOpen && (
          <div className="md:hidden pb-4 space-y-2">
            {links.map((l) => (
              <a key={l.href} href={l.href} onClick={() => setMenuOpen(false)} className="block text-slate-300 hover:text-white text-sm font-medium py-1">
                {l.label}
              </a>
            ))}
          </div>
        )}
      </div>
    </nav>
  );
}

/* ───────────────────────────────── HERO ─────────────────────────────────── */

function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900">
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-indigo-500/20 rounded-full blur-3xl animate-pulse" />
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-violet-500/20 rounded-full blur-3xl animate-pulse" style={{ animationDelay: "1s" }} />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-indigo-600/5 rounded-full blur-3xl" />
      </div>

      <div className="relative z-10 max-w-5xl mx-auto px-4 text-center">
        <div className="inline-flex items-center gap-2 bg-indigo-500/10 border border-indigo-500/20 rounded-full px-4 py-2 mb-8">
          <Sparkles className="w-4 h-4 text-indigo-400" />
          <span className="text-indigo-300 text-sm font-medium">Data Science Course Project — 3 Tasks</span>
        </div>

        <h1 className="text-4xl sm:text-5xl md:text-7xl font-extrabold text-white mb-6 leading-tight">
          Video Game Sales
          <br />
          <span className="bg-gradient-to-r from-indigo-400 via-violet-400 to-purple-400 bg-clip-text text-transparent">
            Web Scraping & ML
          </span>
          <br />
          Analysis
        </h1>

        <p className="text-lg sm:text-xl text-slate-400 max-w-2xl mx-auto mb-10 leading-relaxed">
          A complete end-to-end Data Science project with{" "}
          <span className="text-white font-semibold">Jupyter Notebooks</span>,{" "}
          <span className="text-white font-semibold">Streamlit Dashboards</span>,{" "}
          <span className="text-white font-semibold">6 ML Regression Models</span>, and
          professional documentation.
        </p>

        <div className="flex flex-wrap justify-center gap-4">
          <a href="#overview" className="inline-flex items-center gap-2 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-6 py-3 rounded-xl transition-colors shadow-lg shadow-indigo-600/30">
            Explore Project <ArrowRight className="w-4 h-4" />
          </a>
          <a href="#setup" className="inline-flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold px-6 py-3 rounded-xl border border-slate-700 transition-colors">
            <Terminal className="w-4 h-4" /> Setup Guide
          </a>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-16 max-w-3xl mx-auto">
          {[
            { label: "Dataset Rows", value: "16,500+" },
            { label: "ML Models", value: "6" },
            { label: "Analysis Questions", value: "25" },
            { label: "Project Files", value: "8" },
          ].map((s) => (
            <div key={s.label} className="bg-slate-800/50 rounded-xl p-4 border border-slate-700/50">
              <div className="text-2xl font-bold text-white">{s.value}</div>
              <div className="text-sm text-slate-400 mt-1">{s.label}</div>
            </div>
          ))}
        </div>

        <div className="mt-12">
          <ChevronDown className="w-8 h-8 text-slate-500 animate-bounce mx-auto" />
        </div>
      </div>
    </section>
  );
}

/* ──────────────────────────────── OVERVIEW ──────────────────────────────── */

function Overview() {
  return (
    <section id="overview" className="py-24 bg-slate-950">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">Project Overview</h2>
          <p className="text-slate-400 max-w-2xl mx-auto text-lg">
            Three comprehensive data science tasks covering analysis, web scraping, and machine learning.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {/* Task 1 Card */}
          <div className="group bg-gradient-to-br from-indigo-950/80 to-slate-900 rounded-2xl p-6 border border-indigo-500/20 hover:border-indigo-500/40 transition-all hover:shadow-xl hover:shadow-indigo-500/10">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-indigo-500/20 rounded-xl"><Gamepad2 className="w-6 h-6 text-indigo-400" /></div>
              <div><h3 className="text-lg font-bold text-white">Task 1</h3><p className="text-indigo-300 text-xs">Dataset Analysis & Visualization</p></div>
            </div>
            <p className="text-slate-300 text-sm mb-4 leading-relaxed">
              Analyze a <strong className="text-white">video game sales dataset</strong> with 16,500+ rows. Complete data quality assessment, preprocessing, and 15 analytical questions.
            </p>
            <ul className="space-y-1.5">
              {["Real raw dataset with quality issues", "15 analytical questions + visualizations", "Interactive Streamlit dashboard"].map((item) => (
                <li key={item} className="flex items-start gap-2 text-slate-400 text-xs"><CheckCircle2 className="w-3.5 h-3.5 text-indigo-400 mt-0.5 shrink-0" />{item}</li>
              ))}
            </ul>
          </div>

          {/* Task 2 Card */}
          <div className="group bg-gradient-to-br from-amber-950/40 to-slate-900 rounded-2xl p-6 border border-amber-500/20 hover:border-amber-500/40 transition-all hover:shadow-xl hover:shadow-amber-500/10">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-amber-500/20 rounded-xl"><BookOpen className="w-6 h-6 text-amber-400" /></div>
              <div><h3 className="text-lg font-bold text-white">Task 2</h3><p className="text-amber-300 text-xs">Web Scraping & Domain Analysis</p></div>
            </div>
            <p className="text-slate-300 text-sm mb-4 leading-relaxed">
              Scrape <strong className="text-white">1,000 books</strong> from books.toscrape.com. Build a clean dataset and analyze pricing, ratings, and categories.
            </p>
            <ul className="space-y-1.5">
              {["Web scraping with pagination (50 pages)", "Data extraction & cleaning pipeline", "5 domain analysis questions"].map((item) => (
                <li key={item} className="flex items-start gap-2 text-slate-400 text-xs"><CheckCircle2 className="w-3.5 h-3.5 text-amber-400 mt-0.5 shrink-0" />{item}</li>
              ))}
            </ul>
          </div>

          {/* Task 3 Card */}
          <div className="group bg-gradient-to-br from-emerald-950/40 to-slate-900 rounded-2xl p-6 border border-emerald-500/20 hover:border-emerald-500/40 transition-all hover:shadow-xl hover:shadow-emerald-500/10">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-3 bg-emerald-500/20 rounded-xl"><Cpu className="w-6 h-6 text-emerald-400" /></div>
              <div><h3 className="text-lg font-bold text-white">Task 3</h3><p className="text-emerald-300 text-xs">ML Regression Models</p></div>
            </div>
            <p className="text-slate-300 text-sm mb-4 leading-relaxed">
              Build and compare <strong className="text-white">6 regression models</strong> to predict video game global sales using scikit-learn and XGBoost.
            </p>
            <ul className="space-y-1.5">
              {["6 ML models trained & evaluated", "Hyperparameter tuning with CV", "Feature importance & dashboard"].map((item) => (
                <li key={item} className="flex items-start gap-2 text-slate-400 text-xs"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 mt-0.5 shrink-0" />{item}</li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ────────────────────────────── TASK 1 DETAIL ────────────────────────────── */

const task1Questions = [
  "What is the overall distribution of global video game sales?",
  "Which game genre has the most titles in the dataset?",
  "What are the top 10 best-selling video games of all time?",
  "How have global video game sales changed over the years?",
  "Which gaming platform has the highest total global sales?",
  "What is the market share of each sales region?",
  "Which publishers have released the most game titles?",
  "How do average sales differ across game genres?",
  "How do sales trends differ across regions over time?",
  "Which are the top 5 game genres for each major platform?",
  "Is there a trend in the number of new games released per year?",
  "Which year had the highest total global sales and why?",
  "What is the average global sales per game by genre?",
  "How has platform popularity changed over the decades?",
  "Which publishers dominate sales in each global region?",
];

const task1Insights = [
  "The gaming market is extremely top-heavy — a few blockbusters dominate sales.",
  "Action is the most common genre, but Platform games have higher average sales.",
  "Wii Sports is the best-selling game, largely due to console bundling.",
  "The industry peaked around 2008-2009 during the PS2/Wii/X360 era.",
  "PS2 has the highest total global sales of any platform.",
  "North America contributes roughly 50% of all global video game sales.",
  "EA leads in number of titles; Nintendo leads in total revenue per title.",
  "Genre performance varies significantly — some genres are more profitable per game.",
  "Japan had an earlier peak in the mid-1990s compared to other regions.",
  "Platform preferences differ by genre — Wii favors casual, PS3/X360 favor core games.",
  "Game releases grew until 2008, then declined with the digital shift.",
  "2008 was the best year due to blockbuster titles across multiple platforms.",
  "Mean-median gap is huge — most games sell modestly, a few sell enormously.",
  "Each decade has a dominant platform that reflects the console generation.",
  "Nintendo dominates globally; regional publishers have strong home-market advantage.",
];

function Task1Section() {
  return (
    <section id="task1" className="py-24 bg-gradient-to-b from-slate-950 to-slate-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-indigo-500/10 border border-indigo-500/20 rounded-full px-4 py-2 mb-4">
            <Gamepad2 className="w-4 h-4 text-indigo-400" />
            <span className="text-indigo-300 text-sm font-medium">Task 1</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">Video Game Sales Analysis</h2>
          <p className="text-slate-400 max-w-2xl mx-auto">Complete analysis of a real-world dataset with 16,500+ video game sales records.</p>
        </div>

        <div className="bg-slate-800/50 rounded-2xl p-8 border border-slate-700/50 mb-12">
          <h3 className="text-xl font-bold text-white mb-6 flex items-center gap-2"><Database className="w-5 h-5 text-indigo-400" />Dataset Information</h3>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {[
              { label: "Source", value: "Kaggle / GitHub Mirror" },
              { label: "Size", value: "16,500+ rows × 11 cols" },
              { label: "Issues", value: "Missing values, outliers" },
              { label: "Time Span", value: "1980 — 2023" },
            ].map((d) => (
              <div key={d.label} className="bg-slate-900/50 rounded-xl p-4 border border-slate-700/30">
                <div className="text-sm text-slate-400">{d.label}</div>
                <div className="text-white font-semibold mt-1">{d.value}</div>
              </div>
            ))}
          </div>
        </div>

        <h3 className="text-2xl font-bold text-white mb-6"> 15 Analysis Questions</h3>
        <div className="grid gap-3">
          {task1Questions.map((q, i) => (
            <div key={i} className="bg-slate-800/30 hover:bg-slate-800/50 rounded-xl px-6 py-4 border border-slate-700/30 transition-colors">
              <div className="flex items-start gap-4">
                <span className="shrink-0 w-8 h-8 bg-indigo-500/20 text-indigo-400 rounded-lg flex items-center justify-center text-sm font-bold">{i + 1}</span>
                <div className="flex-1">
                  <p className="text-white font-medium">{q}</p>
                  <p className="text-slate-500 text-sm mt-1">💡 {task1Insights[i]}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ────────────────────────────── TASK 2 DETAIL ────────────────────────────── */

const task2Questions = [
  "What is the distribution of book prices across the catalog?",
  "Which book categories have the most titles?",
  "Is there a relationship between book price and rating?",
  "Which categories have the highest and lowest average prices?",
  "What is the distribution of book ratings across all books?",
];

const task2Insights = [
  "Prices are fairly evenly distributed between £10-£60 with an average around £35.",
  "Some categories like Fiction and Fantasy have significantly more titles than niche categories.",
  "No meaningful correlation — expensive books are not consistently rated higher.",
  "Specialized categories (Philosophy, Science) tend to be more expensive than mainstream ones.",
  "Strong positive bias — most books are rated 4 or 5 stars, suggesting quality curation.",
];

function Task2Section() {
  return (
    <section id="task2" className="py-24 bg-gradient-to-b from-slate-900 to-slate-950">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-amber-500/10 border border-amber-500/20 rounded-full px-4 py-2 mb-4">
            <Globe className="w-4 h-4 text-amber-400" />
            <span className="text-amber-300 text-sm font-medium">Task 2</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">Web Scraping: Books Domain</h2>
          <p className="text-slate-400 max-w-2xl mx-auto">Scraped 1,000 books from books.toscrape.com and analyzed pricing, ratings, and categories.</p>
        </div>

        <div className="bg-slate-800/50 rounded-2xl p-8 border border-slate-700/50 mb-12">
          <h3 className="text-xl font-bold text-white mb-6 flex items-center gap-2"><Globe className="w-5 h-5 text-amber-400" />Scraping Details</h3>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {[
              { label: "Target", value: "books.toscrape.com" },
              { label: "Pages Scraped", value: "50 pages" },
              { label: "Books Collected", value: "1,000" },
              { label: "Library", value: "BeautifulSoup" },
            ].map((d) => (
              <div key={d.label} className="bg-slate-900/50 rounded-xl p-4 border border-slate-700/30">
                <div className="text-sm text-slate-400">{d.label}</div>
                <div className="text-white font-semibold mt-1">{d.value}</div>
              </div>
            ))}
          </div>
        </div>

        <h3 className="text-2xl font-bold text-white mb-6">5 Domain Analysis Questions</h3>
        <div className="grid gap-3">
          {task2Questions.map((q, i) => (
            <div key={i} className="bg-slate-800/30 hover:bg-slate-800/50 rounded-xl px-6 py-4 border border-slate-700/30 transition-colors">
              <div className="flex items-start gap-4">
                <span className="shrink-0 w-8 h-8 bg-amber-500/20 text-amber-400 rounded-lg flex items-center justify-center text-sm font-bold">{i + 1}</span>
                <div className="flex-1">
                  <p className="text-white font-medium">{q}</p>
                  <p className="text-slate-500 text-sm mt-1">💡 {task2Insights[i]}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ────────────────────────────── TASK 3 DETAIL ────────────────────────────── */

const mlModels = [
  { name: "Linear Regression", desc: "Baseline model for comparison", type: "Linear" },
  { name: "Decision Tree", desc: "Non-linear tree-based model", type: "Tree" },
  { name: "Random Forest", desc: "Ensemble of decision trees", type: "Ensemble" },
  { name: "Gradient Boosting", desc: "Sequential boosting ensemble", type: "Boosting" },
  { name: "Extra Trees", desc: "Extremely randomized trees", type: "Ensemble" },
  { name: "XGBoost", desc: "Extreme gradient boosting", type: "Boosting" },
];

const mlPipeline = [
  { step: "1", title: "Data Loading", desc: "Load video game sales dataset from URL" },
  { step: "2", title: "Preprocessing", desc: "Handle missing values, encode categories, scale features" },
  { step: "3", title: "Feature Engineering", desc: "Create Decade, Is_Top_Publisher, Platform_Age features" },
  { step: "4", title: "Model Training", desc: "Train 6 regression models with train/test split" },
  { step: "5", title: "Evaluation", desc: "Compare MAE, MSE, RMSE, R² across all models" },
  { step: "6", title: "Tuning", desc: "RandomizedSearchCV on best model for optimization" },
];

function Task3Section() {
  return (
    <section id="task3" className="py-24 bg-gradient-to-b from-slate-950 to-slate-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 bg-emerald-500/10 border border-emerald-500/20 rounded-full px-4 py-2 mb-4">
            <Cpu className="w-4 h-4 text-emerald-400" />
            <span className="text-emerald-300 text-sm font-medium">Task 3</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">ML Regression — Predicting Game Sales</h2>
          <p className="text-slate-400 max-w-2xl mx-auto">
            Build and compare 6 machine learning regression models to predict global video game sales from platform, genre, publisher, and year.
          </p>
        </div>

        {/* Target & Approach */}
        <div className="grid md:grid-cols-2 gap-6 mb-12">
          <div className="bg-slate-800/50 rounded-2xl p-6 border border-slate-700/50">
            <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
              <span className="text-emerald-400"></span> Prediction Target
            </h3>
            <div className="bg-slate-900/50 rounded-xl p-4 border border-emerald-500/20 mb-4">
              <div className="text-emerald-400 font-mono text-lg font-bold">Global_Sales</div>
              <div className="text-slate-400 text-sm mt-1">Total worldwide sales in millions of units</div>
            </div>
            <p className="text-slate-400 text-sm leading-relaxed">
              We predict how many units a game will sell globally based on its platform, genre, publisher, and release year.
              This is a <strong className="text-white">regression</strong> problem because the target is a continuous number.
            </p>
          </div>
          <div className="bg-slate-800/50 rounded-2xl p-6 border border-slate-700/50">
            <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
              <span className="text-emerald-400"></span> Input Features
            </h3>
            <div className="space-y-3">
              {[
                { feat: "Platform_Encoded", reason: "Different consoles = different market sizes" },
                { feat: "Genre_Encoded", reason: "Some genres sell much better than others" },
                { feat: "Publisher_Encoded", reason: "Major publishers have marketing power" },
                { feat: "Year", reason: "The gaming market has grown over time" },
                { feat: "Is_Top_Publisher", reason: "Top-10 publisher flag (engineered)" },
                { feat: "Platform_Age", reason: "Years since platform launch (engineered)" },
              ].map((f) => (
                <div key={f.feat} className="flex items-center gap-3">
                  <span className="shrink-0 bg-emerald-500/10 text-emerald-400 px-2 py-0.5 rounded text-xs font-mono">{f.feat}</span>
                  <span className="text-slate-500 text-xs">{f.reason}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* ML Pipeline */}
        <h3 className="text-2xl font-bold text-white mb-6">ML Pipeline</h3>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 mb-12">
          {mlPipeline.map((p) => (
            <div key={p.step} className="bg-slate-800/50 rounded-xl p-4 border border-slate-700/50 text-center">
              <div className="w-10 h-10 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center text-lg font-bold mx-auto mb-2">{p.step}</div>
              <div className="text-white font-semibold text-sm">{p.title}</div>
              <div className="text-slate-500 text-xs mt-1">{p.desc}</div>
            </div>
          ))}
        </div>

        {/* 6 Models */}
        <h3 className="text-2xl font-bold text-white mb-6">6 Regression Models</h3>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {mlModels.map((m, i) => {
            const typeColors: Record<string, string> = {
              Linear: "bg-slate-500/20 text-slate-300",
              Tree: "bg-blue-500/20 text-blue-300",
              Ensemble: "bg-violet-500/20 text-violet-300",
              Boosting: "bg-emerald-500/20 text-emerald-300",
            };
            return (
              <div key={m.name} className="bg-slate-800/30 rounded-xl p-5 border border-slate-700/30 hover:border-emerald-500/30 transition-colors">
                <div className="flex items-center gap-3 mb-2">
                  <span className="shrink-0 w-8 h-8 bg-emerald-500/20 text-emerald-400 rounded-lg flex items-center justify-center text-sm font-bold">{i + 1}</span>
                  <div>
                    <div className="text-white font-semibold text-sm">{m.name}</div>
                    <span className={`inline-block px-2 py-0.5 rounded text-xs ${typeColors[m.type]}`}>{m.type}</span>
                  </div>
                </div>
                <p className="text-slate-400 text-xs mt-2">{m.desc}</p>
              </div>
            );
          })}
        </div>

        {/* Evaluation Metrics */}
        <div className="mt-12 bg-slate-800/30 rounded-2xl p-6 border border-slate-700/30">
          <h3 className="text-lg font-bold text-white mb-4">Evaluation Metrics Used</h3>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {[
              { metric: "MAE", full: "Mean Absolute Error", desc: "Average prediction error in millions" },
              { metric: "MSE", full: "Mean Squared Error", desc: "Penalizes large errors more heavily" },
              { metric: "RMSE", full: "Root Mean Squared Error", desc: "Square root of MSE, same units as target" },
              { metric: "R²", full: "R-squared Score", desc: "Proportion of variance explained (0-1)" },
            ].map((m) => (
              <div key={m.metric} className="bg-slate-900/50 rounded-xl p-4 border border-slate-700/30">
                <div className="text-emerald-400 font-bold text-lg">{m.metric}</div>
                <div className="text-white text-sm font-medium">{m.full}</div>
                <div className="text-slate-500 text-xs mt-1">{m.desc}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

/* ────────────────────────────── FILE STRUCTURE ────────────────────────────── */

function FileStructure() {
  const files = [
    { name: "task1_dataset_analysis_visualization.ipynb", icon: "📓", desc: "Task 1 — Jupyter Notebook with 15 analysis questions" },
    { name: "task2_web_scraping_domain_analysis.ipynb", icon: "📓", desc: "Task 2 — Web scraping notebook with 5 domain questions" },
    { name: "task3_ML.ipynb", icon: "🤖", desc: "Task 3 — ML Regression with 6 models, tuning, and dashboard" },
    { name: "task1_dashboard.py", icon: "🐍", desc: "Streamlit dashboard for video game sales analysis" },
    { name: "task2_dashboard.py", icon: "🐍", desc: "Streamlit dashboard for books domain analysis" },
    { name: "README.md", icon: "📄", desc: "Complete project documentation" },
    { name: "requirements.txt", icon: "📋", desc: "Python dependencies list" },
    { name: ".gitignore", icon: "🚫", desc: "Git ignore rules for Python/Jupyter projects" },
  ];

  return (
    <section id="files" className="py-24 bg-slate-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">Project Files</h2>
          <p className="text-slate-400 max-w-2xl mx-auto">All files organized and ready for submission, GitHub, and execution.</p>
        </div>
        <div className="bg-slate-800/30 rounded-2xl border border-slate-700/50 overflow-hidden">
          {files.map((f, i) => (
            <div key={f.name} className={`flex items-start gap-4 px-6 py-4 ${i !== files.length - 1 ? "border-b border-slate-700/30" : ""} hover:bg-slate-800/50 transition-colors`}>
              <span className="text-2xl">{f.icon}</span>
              <div className="flex-1 min-w-0">
                <div className="text-white font-mono text-sm font-semibold truncate">{f.name}</div>
                <div className="text-slate-400 text-sm mt-0.5">{f.desc}</div>
              </div>
              <FileCode2 className="w-5 h-5 text-slate-500 shrink-0 mt-1" />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ──────────────────────────────── SETUP GUIDE ────────────────────────────── */

function SetupGuide() {
  const codeBlocks = [
    { title: "1. Create Virtual Environment", code: `cd data-science-project\npython -m venv venv\n\n# Windows:\nvenv\\Scripts\\activate\n\n# macOS/Linux:\nsource venv/bin/activate` },
    { title: "2. Install Dependencies", code: "pip install -r requirements.txt" },
    { title: "3. Run Jupyter Notebooks", code: `# Option A: Start Jupyter\njupyter notebook\n\n# Option B: Use VS Code\n# Open .ipynb files directly in VS Code` },
    { title: "4. Run Streamlit Dashboards", code: `# Task 1 Dashboard\nstreamlit run task1_dashboard.py\n\n# Task 2 Dashboard\nstreamlit run task2_dashboard.py` },
  ];

  return (
    <section id="setup" className="py-24 bg-gradient-to-b from-slate-950 to-slate-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">Environment Setup</h2>
          <p className="text-slate-400 max-w-2xl mx-auto">Follow these steps to set up and run the project in Visual Studio Code.</p>
        </div>
        <div className="grid gap-6">
          {codeBlocks.map((block) => (
            <div key={block.title} className="bg-slate-800/50 rounded-2xl border border-slate-700/50 overflow-hidden">
              <div className="px-6 py-3 bg-slate-800 border-b border-slate-700/50">
                <h3 className="text-white font-semibold">{block.title}</h3>
              </div>
              <pre className="px-6 py-4 overflow-x-auto">
                <code className="text-emerald-400 text-sm font-mono whitespace-pre">{block.code}</code>
              </pre>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ──────────────────────────────── TECH STACK ─────────────────────────────── */

function TechStack() {
  const categories = [
    { title: "Data Science", color: "indigo", items: ["pandas", "numpy", "scikit-learn"] },
    { title: "Visualization", color: "violet", items: ["matplotlib", "seaborn", "plotly", "missingno"] },
    { title: "Web Scraping", color: "amber", items: ["requests", "beautifulsoup4", "lxml"] },
    { title: "Dashboard", color: "emerald", items: ["streamlit"] },
    { title: "Machine Learning", color: "rose", items: ["xgboost", "scikit-learn"] },
    { title: "Notebook", color: "sky", items: ["jupyter", "notebook", "ipykernel"] },
  ];

  const colorMap: Record<string, string> = {
    indigo: "bg-indigo-500/10 border-indigo-500/30 text-indigo-300",
    violet: "bg-violet-500/10 border-violet-500/30 text-violet-300",
    amber: "bg-amber-500/10 border-amber-500/30 text-amber-300",
    emerald: "bg-emerald-500/10 border-emerald-500/30 text-emerald-300",
    rose: "bg-rose-500/10 border-rose-500/30 text-rose-300",
    sky: "bg-sky-500/10 border-sky-500/30 text-sky-300",
  };

  return (
    <section id="tech" className="py-24 bg-slate-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">Technologies Used</h2>
          <p className="text-slate-400">All libraries and frameworks used in this project.</p>
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {categories.map((cat) => (
            <div key={cat.title} className="bg-slate-800/50 rounded-2xl p-6 border border-slate-700/50">
              <h3 className="text-white font-bold mb-4">{cat.title}</h3>
              <div className="flex flex-wrap gap-2">
                {cat.items.map((item) => (
                  <span key={item} className={`inline-flex items-center px-3 py-1.5 rounded-lg text-sm font-medium border ${colorMap[cat.color]}`}>{item}</span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ──────────────────────────────── FOOTER ─────────────────────────────────── */

function Footer() {
  return (
    <footer className="bg-slate-950 border-t border-slate-800 py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <BarChart3 className="w-5 h-5 text-indigo-400" />
            <span className="text-white font-bold">Data Science Course Project</span>
          </div>
          <p className="text-slate-500 text-sm mb-6 max-w-lg mx-auto">
            A complete end-to-end data science project with video game sales analysis,
            web scraping, machine learning, Jupyter notebooks, and Streamlit dashboards.
          </p>
          <div className="flex justify-center gap-4">
            <a href="https://github.com/Muhammed-Fathi/Video-Game-Sales-Analysis-Web-Scraping-Domain-Analysis" target="_blank" rel="noopener noreferrer" className="text-slate-400 hover:text-white transition-colors flex items-center gap-1">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            </a>
            <a href="https://www.kaggle.com/datasets/gregorut/videogame-sales" target="_blank" rel="noopener noreferrer" className="text-slate-400 hover:text-white transition-colors">
              <ExternalLink className="w-5 h-5" />
            </a>
          </div>
          <div className="mt-8 pt-8 border-t border-slate-800 text-slate-600 text-sm">
            Built with React, Tailwind CSS, Python, Jupyter, Streamlit, and scikit-learn
          </div>
        </div>
      </div>
    </footer>
  );
}

/* ───────────────────────────────── APP ───────────────────────────────────── */

export default function App() {
  return (
    <div className="min-h-screen bg-slate-950" style={{ fontFamily: "'Inter', sans-serif" }}>
      <Navbar />
      <Hero />
      <Overview />
      <Task1Section />
      <Task2Section />
      <Task3Section />
      <FileStructure />
      <SetupGuide />
      <TechStack />
      <Footer />
    </div>
  );
}
