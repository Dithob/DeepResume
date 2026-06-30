"use client";

import {
  BookOpenCheck,
  BriefcaseBusiness,
  ClipboardList,
  Database,
  Gauge,
  UploadCloud
} from "lucide-react";
import type { LucideIcon } from "lucide-react";
import { useEffect, useMemo, useState } from "react";

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000";

type TaskStatus = "todo" | "doing" | "blocked" | "done";

type TaskCheckIn = {
  id: string;
  note: string;
  created_at: string;
};

type TaskDraft = {
  status: TaskStatus;
  actual_hours: string;
  check_in: string;
  completion_notes: string;
  artifact_url: string;
};

type EvidenceType = "project" | "work" | "learning" | "certificate";
type EvidenceStrength = "weak" | "medium" | "strong";

type EvidenceDraft = {
  title: string;
  type: EvidenceType;
  skills: string;
  artifact_url: string;
  source_task_id: string;
  resume_bullet: string;
};

type EvidenceFilters = {
  skill: string;
  source_task_id: string;
  strength: "" | EvidenceStrength;
  has_link: "" | "true" | "false";
};

type ResumeSkill = {
  name: string;
  category: string;
  evidence: string | null;
  confidence: number;
  evidence_strength: "weak" | "medium" | "strong";
};

type ResumeProfile = {
  id: string;
  basics: Record<string, string>;
  skills: ResumeSkill[];
  projects: Record<string, string>[];
  work_experience: Record<string, string>[];
  education: Record<string, string>[];
  raw_text: string;
};

type JobProfile = {
  id: string;
  target_role: string;
  core_skills: string[];
  bonus_skills: string[];
  responsibilities: string[];
  keywords: string[];
  weights: Record<string, number>;
  raw_text: string;
};

type LearningPriority = {
  skill: string;
  priority: string;
  reason: string;
  suggested_task_title: string | null;
  suggested_deliverable: string | null;
  estimated_hours: number;
};

type SkillGapDetail = {
  skill: string;
  requirement_type: "core" | "bonus";
  status: "verified" | "weak_evidence" | "missing";
  priority: "high" | "medium" | "low";
  reason: string;
  evidence: string | null;
  evidence_strength: "weak" | "medium" | "strong" | null;
  suggested_task_title: string;
  suggested_deliverable: string;
  estimated_hours: number;
};

type GapReport = {
  id: string;
  resume_id: string | null;
  job_id: string | null;
  match_score: number;
  strengths: string[];
  missing_core_skills: string[];
  weak_evidence_skills: string[];
  skill_gaps: SkillGapDetail[];
  learning_priorities: LearningPriority[];
  metrics: Record<string, number>;
};

type LearningTask = {
  id: string;
  title: string;
  status: TaskStatus;
  estimated_hours: number;
  actual_hours: number | null;
  deliverable: string;
  skills: string[];
  completion_notes: string | null;
  artifacts: Record<string, string>;
  check_ins: TaskCheckIn[];
};

type LearningMilestone = {
  week: number;
  goal: string;
  tasks: LearningTask[];
};

type LearningPlan = {
  id: string;
  title: string;
  duration_weeks: number;
  weekly_hours: number;
  milestones: LearningMilestone[];
};

type CareerEvidence = {
  id: string;
  title: string;
  type: EvidenceType;
  skills: string[];
  artifacts: Record<string, string>;
  source_task_id: string | null;
  verified: boolean;
  evidence_strength: EvidenceStrength;
  resume_bullets: string[];
};

type EvidenceTrace = {
  evidence_id: string;
  title: string;
  matched_skills: string[];
  artifacts: Record<string, string>;
};

type TailoredResumeDraft = {
  id: string;
  target_role: string;
  markdown: string;
  evidence_trace: EvidenceTrace[];
  unsupported_claims: string[];
};

const sampleResume = `姓名：无绝
求职方向：AI 应用开发工程师
熟悉 Dify、LangChain、FastAPI、Docker、Redis，并使用 Milvus 与 MySQL 构建 RAG 系统。
项目中结合 RAGAS、Golden Dataset 与 SQL 自纠错评估检索和生成效果。`;

const sampleJd = `AI 应用开发工程师
岗位职责：负责 RAG 问答、Agent workflow、模型服务接口与评估闭环。
必备要求：熟悉 LangChain、FastAPI、向量数据库、Prompt Engineering。
加分项：熟悉 LangGraph、Qdrant、Rerank、RAGAS、Docker。`;

const samplePlan = `# 学习主线与阶段规划
| 阶段 | 时间 | 目标 | 主要内容 | 输出物 |
|---|---:|---|---|---|
| 快速补基础 | 第 1-2 周 | 守住算法题和 CS 基础 | 数据结构、Python、MySQL、Redis | 每天 2-3 题；整理错题 |
| RAG / Agent 应用 | 第 3-4 周 | 把项目深挖到可面试 | RAG、Agent、Text-to-SQL | 每个项目准备 10 个追问答案 |`;

const navItems: Array<{ label: string; href: string; icon: LucideIcon; tone: string }> = [
  {
    label: "导入",
    href: "#import",
    icon: UploadCloud,
    tone: "bg-blue-50 text-blue-800 hover:bg-blue-100 dark:bg-blue-950 dark:text-blue-200 dark:hover:bg-blue-900"
  },
  {
    label: "差距分析",
    href: "#gap",
    icon: Gauge,
    tone: "bg-rose-50 text-rose-800 hover:bg-rose-100 dark:bg-rose-950 dark:text-rose-200 dark:hover:bg-rose-900"
  },
  {
    label: "计划导入",
    href: "#plan",
    icon: ClipboardList,
    tone: "bg-amber-50 text-amber-800 hover:bg-amber-100 dark:bg-amber-950 dark:text-amber-200 dark:hover:bg-amber-900"
  },
  {
    label: "看板",
    href: "#board",
    icon: ClipboardList,
    tone: "bg-orange-50 text-orange-800 hover:bg-orange-100 dark:bg-orange-950 dark:text-orange-200 dark:hover:bg-orange-900"
  },
  {
    label: "证据库",
    href: "#evidence",
    icon: Database,
    tone: "bg-emerald-50 text-emerald-800 hover:bg-emerald-100 dark:bg-emerald-950 dark:text-emerald-200 dark:hover:bg-emerald-900"
  },
  {
    label: "简历草稿",
    href: "#resume-draft",
    icon: BookOpenCheck,
    tone: "bg-lime-50 text-lime-800 hover:bg-lime-100 dark:bg-lime-950 dark:text-lime-200 dark:hover:bg-lime-900"
  },
  {
    label: "接口",
    href: "#api",
    icon: Database,
    tone: "bg-sky-50 text-sky-800 hover:bg-sky-100 dark:bg-sky-950 dark:text-sky-200 dark:hover:bg-sky-900"
  }
];

export default function Home() {
  const [resumeText, setResumeText] = useState(sampleResume);
  const [jdText, setJdText] = useState(sampleJd);
  const [planMarkdown, setPlanMarkdown] = useState(samplePlan);
  const [resumeFile, setResumeFile] = useState<File | null>(null);

  const [resume, setResume] = useState<ResumeProfile | null>(null);
  const [job, setJob] = useState<JobProfile | null>(null);
  const [gapReport, setGapReport] = useState<GapReport | null>(null);
  const [plan, setPlan] = useState<LearningPlan | null>(null);
  const [evidence, setEvidence] = useState<CareerEvidence[]>([]);
  const [resumeDraft, setResumeDraft] = useState<TailoredResumeDraft | null>(null);
  const [evidenceDraft, setEvidenceDraft] = useState<EvidenceDraft>({
    title: "",
    type: "learning",
    skills: "",
    artifact_url: "",
    source_task_id: "",
    resume_bullet: ""
  });
  const [evidenceFilters, setEvidenceFilters] = useState<EvidenceFilters>({
    skill: "",
    source_task_id: "",
    strength: "",
    has_link: ""
  });

  const [isBusy, setIsBusy] = useState(false);
  const [statusMessage, setStatusMessage] = useState("Ready");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [taskDrafts, setTaskDrafts] = useState<Record<string, TaskDraft>>({});

  const tasks = useMemo(() => plan?.milestones.flatMap((milestone) => milestone.tasks) ?? [], [plan]);
  const doneCount = tasks.filter((task) => task.status === "done").length;

  useEffect(() => {
    void refreshEvidence();
  }, []);

  async function parseResume() {
    await runAction("Resume parsed", async () => {
      const parsed = await postJson<ResumeProfile>("/api/resumes/parse", { resume_text: resumeText });
      setResume(parsed);
      setGapReport(null);
      setResumeDraft(null);
    });
  }

  async function parseResumeFile() {
    if (!resumeFile) {
      setErrorMessage("请先选择 Markdown 或文本简历文件。");
      return;
    }
    await runAction("Resume file parsed", async () => {
      const formData = new FormData();
      formData.append("file", resumeFile);
      const parsed = await postFormData<ResumeProfile>("/api/resumes/parse-file", formData);
      setResume(parsed);
      setResumeText(parsed.raw_text);
      setGapReport(null);
      setResumeDraft(null);
    });
  }

  async function parseJob() {
    await runAction("JD parsed", async () => {
      const parsed = await postJson<JobProfile>("/api/jobs/parse", { jd_text: jdText });
      setJob(parsed);
      setGapReport(null);
      setResumeDraft(null);
    });
  }

  async function analyzeGap() {
    if (!resume || !job) {
      setErrorMessage("请先解析简历和 JD。");
      return;
    }
    await runAction("Gap report generated", async () => {
      const report = await postJson<GapReport>("/api/gap/analyze", {
        resume_id: resume.id,
        job_id: job.id
      });
      setGapReport(report);
    });
  }

  async function generatePlan() {
    if (!gapReport) {
      setErrorMessage("请先生成差距分析。");
      return;
    }
    await runAction("Learning plan generated", async () => {
      const generated = await postJson<LearningPlan>("/api/plans/generate", {
        gap_report_id: gapReport.id,
        weekly_hours: 8,
        duration_weeks: 4
      });
      setPlan(generated);
    });
  }

  async function importPlan() {
    await runAction("Learning plan imported", async () => {
      const imported = await postJson<LearningPlan>("/api/plans/import", {
        markdown: planMarkdown,
        weekly_hours: 8
      });
      setPlan(imported);
    });
  }

  function getTaskDraft(task: LearningTask): TaskDraft {
    return taskDrafts[task.id] ?? createTaskDraft(task);
  }

  function updateTaskDraft(taskId: string, patch: Partial<TaskDraft>) {
    setTaskDrafts((current) => ({
      ...current,
      [taskId]: {
        ...(current[taskId] ?? createTaskDraft(findTaskById(tasks, taskId))),
        ...patch
      }
    }));
  }

  async function saveTaskProgress(task: LearningTask, options: { complete?: boolean; createEvidence?: boolean } = {}) {
    const draft = getTaskDraft(task);
    const artifactUrl = draft.artifact_url.trim();
    const artifacts = artifactUrl ? { ...task.artifacts, artifact_url: artifactUrl } : task.artifacts;
    const completionNotes = draft.completion_notes.trim() || task.completion_notes || "";
    const checkIn = draft.check_in.trim();
    const status = options.complete ? "done" : draft.status;

    if (status === "done" && !completionNotes && !Object.values(artifacts).some((value) => value.trim())) {
      setErrorMessage("完成任务前请填写完成备注或产物链接。");
      return;
    }

    await runAction(options.createEvidence ? "Task completed and evidence created" : "Task progress saved", async () => {
      const updated = await patchJson<LearningTask>(`/api/tasks/${task.id}`, {
        status,
        actual_hours: draft.actual_hours ? Number(draft.actual_hours) : task.actual_hours,
        check_in: checkIn || undefined,
        completion_notes: completionNotes || undefined,
        artifacts
      });
      setPlan((current) => replaceTaskInPlan(current, updated));
      setTaskDrafts((current) => ({
        ...current,
        [updated.id]: {
          ...createTaskDraft(updated),
          check_in: "",
          artifact_url: ""
        }
      }));

      if (options.createEvidence) {
        const created = await postJson<CareerEvidence>("/api/evidence", {
          source_task_id: updated.id
        });
        setEvidence((current) => [created, ...current.filter((item) => item.id !== created.id)]);
      }
    });
  }

  async function refreshEvidence() {
    try {
      const params = new URLSearchParams();
      if (evidenceFilters.skill.trim()) {
        params.set("skill", evidenceFilters.skill.trim());
      }
      if (evidenceFilters.source_task_id.trim()) {
        params.set("source_task_id", evidenceFilters.source_task_id.trim());
      }
      if (evidenceFilters.strength) {
        params.set("strength", evidenceFilters.strength);
      }
      if (evidenceFilters.has_link) {
        params.set("has_link", evidenceFilters.has_link);
      }
      const items = await getJson<CareerEvidence[]>(`/api/evidence${params.toString() ? `?${params.toString()}` : ""}`);
      setEvidence(items);
    } catch {
      // Backend may not be started yet; keep the initial page usable.
    }
  }

  async function createManualEvidence() {
    const skills = splitListInput(evidenceDraft.skills);
    const artifactUrl = evidenceDraft.artifact_url.trim();
    const sourceTaskId = evidenceDraft.source_task_id.trim();
    const resumeBullet = evidenceDraft.resume_bullet.trim();

    if (!evidenceDraft.title.trim()) {
      setErrorMessage("请填写证据标题。");
      return;
    }

    await runAction("Evidence created", async () => {
      const created = await postJson<CareerEvidence>("/api/evidence", {
        title: evidenceDraft.title.trim(),
        type: evidenceDraft.type,
        skills,
        artifacts: artifactUrl ? { artifact_url: artifactUrl } : {},
        source_task_id: sourceTaskId || undefined,
        resume_bullets: resumeBullet ? [resumeBullet] : []
      });
      setEvidence((current) => [created, ...current.filter((item) => item.id !== created.id)]);
      setEvidenceDraft({
        title: "",
        type: "learning",
        skills: "",
        artifact_url: "",
        source_task_id: "",
        resume_bullet: ""
      });
    });
  }

  async function assembleResumeDraft() {
    if (!resume || !job) {
      setErrorMessage("请先解析简历和 JD。");
      return;
    }
    await runAction("Resume draft assembled", async () => {
      const draft = await postJson<TailoredResumeDraft>("/api/resumes/assemble", {
        resume_id: resume.id,
        job_id: job.id,
        evidence_ids: evidence.map((item) => item.id)
      });
      setResumeDraft(draft);
    });
  }

  async function runAction(successMessage: string, action: () => Promise<void>) {
    setIsBusy(true);
    setErrorMessage(null);
    setStatusMessage("Working...");
    try {
      await action();
      setStatusMessage(successMessage);
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : "Request failed.");
      setStatusMessage("Request failed");
    } finally {
      setIsBusy(false);
    }
  }

  return (
    <main className="min-h-screen bg-[#f6f7f1] text-zinc-900 dark:bg-zinc-950 dark:text-zinc-100">
      <div className="mx-auto grid max-w-7xl gap-4 px-4 py-12 md:gap-6 md:px-6 md:py-16 lg:px-8 lg:py-20 2xl:max-w-[calc(80rem+244px)] 2xl:grid-cols-[minmax(0,80rem)_220px]">
        <div className="grid gap-4 md:gap-6">
        <header className="grid grid-cols-1 gap-4 md:gap-6 lg:grid-cols-12">
          <BentoCard className="bg-blue-50 dark:bg-blue-950 lg:col-span-8">
            <div className="grid gap-6">
              <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
                <div className="max-w-3xl">
                  <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-blue-700 text-white dark:bg-blue-300 dark:text-blue-950">
                    <BriefcaseBusiness size={22} />
                  </div>
                  <h1 className="text-3xl font-semibold text-zinc-900 dark:text-zinc-100 md:text-4xl">
                    CV2Offer Agent 工作台
                  </h1>
                  <p className="mt-3 max-w-2xl text-sm leading-6 text-zinc-600 dark:text-zinc-400 md:text-base">
                    用简历、岗位需求和学习计划形成闭环：先看差距，再安排任务，最后把完成结果沉淀成可复用的职业证据。
                  </p>
                </div>
              </div>
              <div className="rounded-xl bg-white p-4 text-sm text-zinc-700 dark:bg-blue-900 dark:text-blue-100">
                {statusMessage}
                {errorMessage ? <span className="ml-4 text-red-700 dark:text-red-300">{errorMessage}</span> : null}
              </div>
            </div>
          </BentoCard>

          <BentoCard className="bg-emerald-50 dark:bg-emerald-950 lg:col-span-4">
            <div className="grid h-full content-between gap-6">
              <BentoTitle icon={<Gauge size={18} />} title="当前进度" tone="emerald" />
              <div className="grid grid-cols-3 gap-4">
                <Metric label="Match" value={gapReport ? String(gapReport.match_score) : "-"} />
                <Metric label="Tasks" value={`${doneCount}/${tasks.length}`} />
                <Metric label="Evidence" value={String(evidence.length)} />
              </div>
              <p className="text-sm leading-6 text-zinc-600 dark:text-zinc-400">
                MVP 仍然使用 rule-based 解析与分析，适合先验证学习闭环，后续再替换为真实 AI adapter。
              </p>
            </div>
          </BentoCard>
        </header>

        <MobileNav />

        <section className="grid grid-cols-1 gap-4 md:gap-6 lg:grid-cols-12">
          <BentoCard id="import" className="scroll-mt-28 bg-white dark:bg-zinc-900 lg:col-span-7">
            <div className="grid gap-6">
              <BentoTitle icon={<UploadCloud size={18} />} title="导入简历与 JD" tone="blue" />
              <div className="grid gap-4 md:grid-cols-2 md:gap-6">
                <TextBox label="Resume / Markdown" value={resumeText} onChange={setResumeText} />
                <TextBox label="Target JD" value={jdText} onChange={setJdText} />
              </div>
              <div className="grid gap-4 rounded-xl bg-blue-50 p-4 dark:bg-blue-950 md:grid-cols-[minmax(0,1fr)_auto] md:items-end">
                <label className="grid gap-4 text-sm">
                  <span className="font-medium text-zinc-900 dark:text-zinc-100">CV file</span>
                  <input
                    accept=".md,.txt,text/markdown,text/plain"
                    className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 file:mr-4 file:rounded-xl file:border-0 file:bg-blue-100 file:px-4 file:py-2 file:text-blue-800 dark:text-zinc-100 dark:file:bg-blue-900 dark:file:text-blue-100 md:px-4 md:py-3"
                    type="file"
                    onChange={(event) => setResumeFile(event.target.files?.[0] ?? null)}
                  />
                </label>
                <ActionButton disabled={isBusy || !resumeFile} onClick={parseResumeFile} variant="secondary">
                  Parse CV file
                </ActionButton>
              </div>
              <div className="flex flex-wrap gap-4">
                <ActionButton disabled={isBusy} onClick={parseResume}>
                  Parse resume
                </ActionButton>
                <ActionButton disabled={isBusy} onClick={parseJob} variant="secondary">
                  Parse JD
                </ActionButton>
                <ActionButton disabled={isBusy || !resume || !job} onClick={analyzeGap}>
                  Generate gap report
                </ActionButton>
              </div>
              <div className="grid gap-4 md:grid-cols-2 md:gap-6">
                <ResultBlock title="Parsed resume">
                  {resume ? (
                    <div className="grid gap-4">
                      <KeyValue label="ID" value={resume.id} />
                      <KeyValue label="Skills" value={resume.skills.map((skill) => skill.name).join(", ") || "-"} />
                    </div>
                  ) : (
                    <EmptyState text="No resume parsed yet." />
                  )}
                </ResultBlock>
                <ResultBlock title="Parsed JD">
                  {job ? (
                    <div className="grid gap-4">
                      <KeyValue label="Role" value={job.target_role} />
                      <KeyValue label="Core" value={job.core_skills.join(", ") || "-"} />
                      <KeyValue label="Bonus" value={job.bonus_skills.join(", ") || "-"} />
                    </div>
                  ) : (
                    <EmptyState text="No JD parsed yet." />
                  )}
                </ResultBlock>
              </div>
            </div>
          </BentoCard>

          <BentoCard id="gap" className="scroll-mt-28 bg-rose-50 dark:bg-rose-950 lg:col-span-5">
            <div className="grid gap-6">
              <BentoTitle icon={<Gauge size={18} />} title="Gap Report" tone="rose" />
              {gapReport ? (
                <>
                  <div className="grid gap-4">
                    <StatusRow label="已覆盖技能" items={gapReport.strengths} tone="good" />
                    <StatusRow label="缺失核心技能" items={gapReport.missing_core_skills} tone="bad" />
                    <StatusRow label="弱证据技能" items={gapReport.weak_evidence_skills} tone="warn" />
                  </div>
                  <div className="grid max-h-[34rem] gap-4 overflow-auto pr-1">
                    {gapReport.skill_gaps.map((gap) => (
                      <GapItem key={`${gap.skill}-${gap.requirement_type}`} gap={gap} />
                    ))}
                  </div>
                  <ActionButton disabled={isBusy} onClick={generatePlan}>
                    Generate 4-week plan
                  </ActionButton>
                </>
              ) : (
                <EmptyState text="Parse resume and JD, then generate a gap report." />
              )}
            </div>
          </BentoCard>

          <BentoCard id="plan" className="scroll-mt-28 bg-amber-50 dark:bg-amber-950 lg:col-span-4">
            <div className="grid gap-6">
              <BentoTitle icon={<ClipboardList size={18} />} title="学习计划导入" tone="amber" />
              <TextBox label="Learning plan Markdown" value={planMarkdown} onChange={setPlanMarkdown} />
              <ActionButton disabled={isBusy} onClick={importPlan}>
                Import Markdown plan
              </ActionButton>
            </div>
          </BentoCard>

          <BentoCard id="board" className="scroll-mt-28 bg-white dark:bg-zinc-900 lg:col-span-8">
            <div className="grid gap-6">
              <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                <BentoTitle icon={<ClipboardList size={18} />} title="周计划看板" tone="orange" />
                {plan ? (
                  <span className="rounded-xl bg-zinc-100 px-4 py-2 text-xs text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400">
                    {plan.duration_weeks} weeks / {plan.weekly_hours} h per week
                  </span>
                ) : null}
              </div>
              {plan ? (
                <div className="grid gap-4 md:grid-cols-2 md:gap-6">
                  {plan.milestones.map((milestone) => (
                    <MilestoneColumn
                      key={`${plan.id}-${milestone.week}`}
                      milestone={milestone}
                      isBusy={isBusy}
                      getTaskDraft={getTaskDraft}
                      updateTaskDraft={updateTaskDraft}
                      saveTaskProgress={saveTaskProgress}
                    />
                  ))}
                </div>
              ) : (
                <EmptyState text="Import Markdown or generate a plan from the gap report." />
              )}
            </div>
          </BentoCard>

          <BentoCard id="evidence" className="scroll-mt-28 bg-emerald-50 dark:bg-emerald-950 lg:col-span-7">
            <div className="grid gap-6">
              <BentoTitle icon={<BookOpenCheck size={18} />} title="Evidence Vault" tone="emerald" />
              <div className="grid gap-4 rounded-xl bg-white p-4 dark:bg-zinc-900">
                <div className="grid gap-4 md:grid-cols-2">
                  <SmallInput
                    label="Skill filter"
                    value={evidenceFilters.skill}
                    onChange={(value) => setEvidenceFilters((current) => ({ ...current, skill: value }))}
                    placeholder="RAGAS"
                  />
                  <SmallInput
                    label="Task filter"
                    value={evidenceFilters.source_task_id}
                    onChange={(value) => setEvidenceFilters((current) => ({ ...current, source_task_id: value }))}
                    placeholder="task_..."
                  />
                  <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
                    Strength
                    <select
                      className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
                      value={evidenceFilters.strength}
                      onChange={(event) =>
                        setEvidenceFilters((current) => ({
                          ...current,
                          strength: event.target.value as EvidenceFilters["strength"]
                        }))
                      }
                    >
                      <option value="">All</option>
                      <option value="weak">weak</option>
                      <option value="medium">medium</option>
                      <option value="strong">strong</option>
                    </select>
                  </label>
                  <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
                    Link
                    <select
                      className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
                      value={evidenceFilters.has_link}
                      onChange={(event) =>
                        setEvidenceFilters((current) => ({
                          ...current,
                          has_link: event.target.value as EvidenceFilters["has_link"]
                        }))
                      }
                    >
                      <option value="">All</option>
                      <option value="true">Has link</option>
                      <option value="false">No link</option>
                    </select>
                  </label>
                </div>
                <div className="flex flex-wrap gap-4">
                  <ActionButton disabled={isBusy} onClick={refreshEvidence} variant="secondary">
                    Apply filters
                  </ActionButton>
                </div>
              </div>
              <div className="grid gap-4 rounded-xl bg-white p-4 dark:bg-zinc-900">
                <div className="grid gap-4 md:grid-cols-2">
                  <SmallInput
                    label="Evidence title"
                    value={evidenceDraft.title}
                    onChange={(value) => setEvidenceDraft((current) => ({ ...current, title: value }))}
                    placeholder="RAG 评估闭环复盘"
                  />
                  <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
                    Type
                    <select
                      className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
                      value={evidenceDraft.type}
                      onChange={(event) =>
                        setEvidenceDraft((current) => ({ ...current, type: event.target.value as EvidenceType }))
                      }
                    >
                      <option value="learning">learning</option>
                      <option value="project">project</option>
                      <option value="work">work</option>
                      <option value="certificate">certificate</option>
                    </select>
                  </label>
                  <SmallInput
                    label="Skills"
                    value={evidenceDraft.skills}
                    onChange={(value) => setEvidenceDraft((current) => ({ ...current, skills: value }))}
                    placeholder="RAGAS, FastAPI"
                  />
                  <SmallInput
                    label="Source task"
                    value={evidenceDraft.source_task_id}
                    onChange={(value) => setEvidenceDraft((current) => ({ ...current, source_task_id: value }))}
                    placeholder="可选 task_id"
                  />
                  <SmallInput
                    label="Artifact link"
                    value={evidenceDraft.artifact_url}
                    onChange={(value) => setEvidenceDraft((current) => ({ ...current, artifact_url: value }))}
                    placeholder="https://github.com/..."
                  />
                  <SmallInput
                    label="Resume bullet"
                    value={evidenceDraft.resume_bullet}
                    onChange={(value) => setEvidenceDraft((current) => ({ ...current, resume_bullet: value }))}
                    placeholder="用 RAGAS 搭建评估闭环"
                  />
                </div>
                <div className="flex flex-wrap gap-4">
                  <ActionButton disabled={isBusy} onClick={createManualEvidence}>
                    Create evidence
                  </ActionButton>
                </div>
              </div>
              {evidence.length > 0 ? (
                <div className="grid gap-4 md:grid-cols-2 md:gap-6">
                  {evidence.map((item) => (
                    <EvidenceItem key={item.id} item={item} />
                  ))}
                </div>
              ) : (
                <EmptyState text="Complete a task to create career evidence." />
              )}
            </div>
          </BentoCard>

          <BentoCard id="resume-draft" className="scroll-mt-28 bg-lime-50 dark:bg-lime-950 lg:col-span-7">
            <div className="grid gap-6">
              <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                <BentoTitle icon={<BookOpenCheck size={18} />} title="定向简历草稿" tone="sky" />
                <ActionButton disabled={isBusy || !resume || !job} onClick={assembleResumeDraft}>
                  Assemble resume
                </ActionButton>
              </div>
              {resumeDraft ? (
                <div className="grid gap-4">
                  <div className="grid gap-4 md:grid-cols-2">
                    <ResultBlock title="Evidence trace">
                      {resumeDraft.evidence_trace.length > 0 ? (
                        <div className="grid gap-4">
                          {resumeDraft.evidence_trace.map((trace) => (
                            <div key={trace.evidence_id} className="grid gap-4">
                              <KeyValue label={trace.title} value={trace.matched_skills.join(", ") || "-"} />
                            </div>
                          ))}
                        </div>
                      ) : (
                        <EmptyState text="No evidence matches current JD skills." />
                      )}
                    </ResultBlock>
                    <ResultBlock title="Unsupported claims">
                      {resumeDraft.unsupported_claims.length > 0 ? (
                        <div className="flex flex-wrap gap-4">
                          {resumeDraft.unsupported_claims.map((claim) => (
                            <Badge key={claim} text={claim} tone="warn" />
                          ))}
                        </div>
                      ) : (
                        <EmptyState text="No unsupported core skills." />
                      )}
                    </ResultBlock>
                  </div>
                  <pre className="max-h-[32rem] overflow-auto whitespace-pre-wrap rounded-xl bg-white p-4 text-sm leading-6 text-zinc-800 dark:bg-zinc-900 dark:text-zinc-200">
                    {resumeDraft.markdown}
                  </pre>
                </div>
              ) : (
                <EmptyState text="Parse resume and JD, create evidence, then assemble a JD-targeted Markdown resume draft." />
              )}
            </div>
          </BentoCard>

          <BentoCard id="api" className="scroll-mt-28 bg-sky-50 dark:bg-sky-950 lg:col-span-5">
            <div className="grid gap-6">
              <BentoTitle icon={<Database size={18} />} title="数据接口状态" tone="sky" />
              <div className="grid gap-4">
                <KeyValue label="API base" value={API_BASE} />
                <KeyValue label="Resume ID" value={resume?.id ?? "-"} />
                <KeyValue label="Job ID" value={job?.id ?? "-"} />
                <KeyValue label="Plan ID" value={plan?.id ?? "-"} />
                <KeyValue label="Draft ID" value={resumeDraft?.id ?? "-"} />
              </div>
            </div>
          </BentoCard>
        </section>
        </div>
        <SideNav />
      </div>
    </main>
  );
}

async function getJson<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`);
  return parseResponse<T>(response);
}

async function postJson<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  return parseResponse<T>(response);
}

async function postFormData<T>(path: string, body: FormData): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    body
  });
  return parseResponse<T>(response);
}

async function patchJson<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  return parseResponse<T>(response);
}

async function parseResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let message = `${response.status} ${response.statusText}`;
    try {
      const payload = (await response.json()) as { detail?: string };
      message = payload.detail ?? message;
    } catch {
      // Keep the HTTP status fallback.
    }
    throw new Error(message);
  }
  return (await response.json()) as T;
}

function replaceTaskInPlan(plan: LearningPlan | null, task: LearningTask): LearningPlan | null {
  if (!plan) {
    return plan;
  }
  return {
    ...plan,
    milestones: plan.milestones.map((milestone) => ({
      ...milestone,
      tasks: milestone.tasks.map((item) => (item.id === task.id ? task : item))
    }))
  };
}

function createTaskDraft(task: LearningTask | undefined): TaskDraft {
  return {
    status: task?.status ?? "todo",
    actual_hours: task?.actual_hours != null ? String(task.actual_hours) : "",
    check_in: "",
    completion_notes: task?.completion_notes ?? "",
    artifact_url: ""
  };
}

function findTaskById(tasks: LearningTask[], taskId: string): LearningTask | undefined {
  return tasks.find((task) => task.id === taskId);
}

function splitListInput(value: string): string[] {
  return value
    .split(/[,，、\n]/)
    .map((item) => item.trim())
    .filter(Boolean);
}

function SideNav() {
  return (
    <aside className="hidden 2xl:block">
      <nav className="sticky top-8 rounded-2xl border border-zinc-100 bg-white p-4 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
        <a className="mb-4 inline-flex items-center gap-4 rounded-xl px-4 py-2 font-semibold text-zinc-900 transition-colors hover:bg-zinc-100 focus:outline-none focus:ring-2 focus:ring-blue-500/20 dark:text-zinc-100 dark:hover:bg-zinc-800 md:px-6 md:py-3" href="#">
          <BriefcaseBusiness size={18} />
          <span>CV2Offer</span>
        </a>
        <div className="grid gap-4">
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <a
                key={item.href}
                className={`px-4 py-2 md:px-6 md:py-3 rounded-xl font-medium transition-colors inline-flex items-center gap-4 focus:outline-none focus:ring-2 focus:ring-blue-500/20 active:scale-95 ${item.tone}`}
                href={item.href}
              >
                <Icon size={16} />
                <span>{item.label}</span>
              </a>
            );
          })}
        </div>
      </nav>
    </aside>
  );
}

function MobileNav() {
  return (
    <nav className="rounded-2xl border border-zinc-100 bg-white p-4 shadow-sm dark:border-zinc-800 dark:bg-zinc-900 2xl:hidden">
      <div className="flex flex-wrap gap-4">
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <a
              key={item.href}
              className={`px-4 py-2 md:px-6 md:py-3 rounded-xl font-medium transition-colors inline-flex items-center gap-4 focus:outline-none focus:ring-2 focus:ring-blue-500/20 active:scale-95 ${item.tone}`}
              href={item.href}
            >
              <Icon size={16} />
              <span>{item.label}</span>
            </a>
          );
        })}
      </div>
    </nav>
  );
}

function BentoCard({
  id,
  className = "",
  children
}: {
  id?: string;
  className?: string;
  children: React.ReactNode;
}) {
  return (
    <section
      id={id}
      className={`rounded-2xl border border-zinc-100 dark:border-zinc-800 bg-white p-4 shadow-sm hover:shadow-md hover:-translate-y-0.5 transition-all duration-200 motion-reduce:transform-none motion-reduce:transition-none dark:bg-zinc-900 md:p-6 ${className}`}
    >
      {children}
    </section>
  );
}

function BentoTitle({
  icon,
  title,
  tone = "blue"
}: {
  icon: React.ReactNode;
  title: string;
  tone?: "blue" | "rose" | "amber" | "orange" | "emerald" | "sky";
}) {
  const toneClass = {
    blue: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-100",
    rose: "bg-rose-100 text-rose-800 dark:bg-rose-900 dark:text-rose-100",
    amber: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-100",
    orange: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-100",
    emerald: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-100",
    sky: "bg-sky-100 text-sky-800 dark:bg-sky-900 dark:text-sky-100"
  }[tone];

  return (
    <div className="flex items-center gap-4">
      <span className={`flex h-10 w-10 items-center justify-center rounded-xl ${toneClass}`}>
        {icon}
      </span>
      <h2 className="text-xl font-semibold text-zinc-900 dark:text-zinc-100 md:text-2xl">{title}</h2>
    </div>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-zinc-50 px-4 py-4 text-center dark:bg-zinc-800">
      <div className="text-xl font-semibold text-zinc-900 dark:text-zinc-100 md:text-2xl">{value}</div>
      <div className="mt-1 text-xs text-zinc-600 dark:text-zinc-400">{label}</div>
    </div>
  );
}

function TextBox({ label, value, onChange }: { label: string; value: string; onChange: (value: string) => void }) {
  return (
    <label className="grid gap-4 text-sm">
      <span className="font-medium text-zinc-900 dark:text-zinc-100">{label}</span>
      <textarea
        className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all min-h-52 resize-y px-3 py-2 text-sm leading-6 text-zinc-900 placeholder:text-zinc-400 dark:text-zinc-100 md:px-4 md:py-3"
        value={value}
        onChange={(event) => onChange(event.target.value)}
      />
    </label>
  );
}

function SmallInput({
  label,
  value,
  onChange,
  placeholder
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
}) {
  return (
    <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
      {label}
      <input
        className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 placeholder:text-zinc-400 dark:text-zinc-100 md:px-4 md:py-3"
        placeholder={placeholder}
        value={value}
        onChange={(event) => onChange(event.target.value)}
      />
    </label>
  );
}

function ResultBlock({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="rounded-xl bg-zinc-50 p-4 dark:bg-zinc-800">
      <h3 className="mb-4 text-sm font-semibold text-zinc-900 dark:text-zinc-100">{title}</h3>
      {children}
    </div>
  );
}

function KeyValue({ label, value }: { label: string; value: string }) {
  return (
    <div className="grid gap-4">
      <span className="text-xs font-medium text-zinc-500 dark:text-zinc-400">{label}</span>
      <span className="break-words text-sm leading-6 text-zinc-700 dark:text-zinc-300">{value}</span>
    </div>
  );
}

function EmptyState({ text }: { text: string }) {
  return <p className="rounded-xl bg-zinc-50 p-4 text-sm leading-6 text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400">{text}</p>;
}

function ActionButton({
  children,
  disabled,
  onClick,
  variant = "primary"
}: {
  children: React.ReactNode;
  disabled?: boolean;
  onClick: () => void;
  variant?: "primary" | "secondary";
}) {
  const tone =
    variant === "primary"
      ? "bg-blue-700 text-white hover:bg-blue-800 disabled:bg-zinc-300 disabled:text-zinc-500 dark:bg-blue-300 dark:text-blue-950 dark:hover:bg-blue-200"
      : "bg-white text-zinc-800 hover:bg-zinc-100 disabled:bg-zinc-100 disabled:text-zinc-400 dark:bg-zinc-800 dark:text-zinc-100 dark:hover:bg-zinc-700";

  return (
    <button
      className={`px-4 py-2 md:px-6 md:py-3 rounded-xl font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500/20 active:scale-95 disabled:cursor-not-allowed ${tone}`}
      disabled={disabled}
      type="button"
      onClick={onClick}
    >
      {children}
    </button>
  );
}

function StatusRow({ label, items, tone }: { label: string; items: string[]; tone: "good" | "warn" | "bad" }) {
  const color =
    tone === "good"
      ? "bg-emerald-50 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200"
      : tone === "warn"
        ? "bg-amber-50 text-amber-800 dark:bg-amber-950 dark:text-amber-200"
        : "bg-red-50 text-red-800 dark:bg-red-950 dark:text-red-200";
  return (
    <div className="grid gap-4">
      <div className="text-xs font-medium text-zinc-500 dark:text-zinc-400">{label}</div>
      <div className="flex flex-wrap gap-4">
        {items.length > 0 ? (
          items.map((item) => (
            <span key={item} className={`rounded-xl px-3 py-2 text-xs ${color}`}>
              {item}
            </span>
          ))
        ) : (
          <span className="text-xs text-zinc-500 dark:text-zinc-400">None</span>
        )}
      </div>
    </div>
  );
}

function GapItem({ gap }: { gap: SkillGapDetail }) {
  return (
    <article className="rounded-xl bg-zinc-50 p-4 dark:bg-zinc-800">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <h3 className="font-semibold text-zinc-900 dark:text-zinc-100">{gap.skill}</h3>
          <p className="mt-2 text-sm leading-6 text-zinc-600 dark:text-zinc-400">{gap.reason}</p>
        </div>
        <div className="flex flex-wrap gap-4">
          <Badge text={gap.requirement_type} />
          <Badge text={gap.status} tone={gap.status === "verified" ? "good" : gap.status === "weak_evidence" ? "warn" : "bad"} />
          <Badge text={gap.priority} tone={gap.priority === "high" ? "bad" : gap.priority === "medium" ? "warn" : "good"} />
        </div>
      </div>
      {gap.evidence ? <p className="mt-4 text-xs leading-5 text-zinc-500 dark:text-zinc-400">Evidence: {gap.evidence}</p> : null}
      <p className="mt-4 text-sm leading-6 text-blue-700 dark:text-blue-300">
        Next: {gap.suggested_task_title} / {gap.suggested_deliverable}
      </p>
    </article>
  );
}

function MilestoneColumn({
  milestone,
  isBusy,
  getTaskDraft,
  updateTaskDraft,
  saveTaskProgress
}: {
  milestone: LearningMilestone;
  isBusy: boolean;
  getTaskDraft: (task: LearningTask) => TaskDraft;
  updateTaskDraft: (taskId: string, patch: Partial<TaskDraft>) => void;
  saveTaskProgress: (task: LearningTask, options?: { complete?: boolean; createEvidence?: boolean }) => void;
}) {
  return (
    <section className="rounded-xl bg-zinc-50 p-4 dark:bg-zinc-800">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h3 className="font-semibold text-zinc-900 dark:text-zinc-100">Week {milestone.week}</h3>
          <p className="mt-2 text-sm leading-6 text-zinc-600 dark:text-zinc-400">{milestone.goal}</p>
        </div>
        <span className="rounded-xl bg-white px-3 py-2 text-xs text-zinc-600 dark:bg-zinc-900 dark:text-zinc-400">
          {milestone.tasks.length} task
        </span>
      </div>
      <div className="mt-4 grid gap-4">
        {milestone.tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            draft={getTaskDraft(task)}
            isBusy={isBusy}
            updateTaskDraft={updateTaskDraft}
            saveTaskProgress={saveTaskProgress}
          />
        ))}
      </div>
    </section>
  );
}

function TaskItem({
  task,
  draft,
  isBusy,
  updateTaskDraft,
  saveTaskProgress
}: {
  task: LearningTask;
  draft: TaskDraft;
  isBusy: boolean;
  updateTaskDraft: (taskId: string, patch: Partial<TaskDraft>) => void;
  saveTaskProgress: (task: LearningTask, options?: { complete?: boolean; createEvidence?: boolean }) => void;
}) {
  const lastCheckIn = task.check_ins.at(-1);

  return (
    <article className="rounded-xl bg-white p-4 dark:bg-zinc-900">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <h4 className="font-medium text-zinc-900 dark:text-zinc-100">{task.title}</h4>
        <Badge text={task.status} tone={task.status === "done" ? "good" : task.status === "blocked" ? "bad" : "neutral"} />
      </div>
      <p className="mt-3 text-sm leading-6 text-zinc-600 dark:text-zinc-400">{task.deliverable}</p>
      <div className="mt-4 flex flex-wrap gap-4 text-xs text-zinc-500 dark:text-zinc-400">
        <span>预计 {task.estimated_hours}h</span>
        <span>实际 {task.actual_hours ?? "-"}h</span>
        <span>{task.check_ins.length} check-in</span>
      </div>
      <div className="mt-4 flex flex-wrap gap-4">
        {task.skills.map((skill) => (
          <Badge key={skill} text={skill} />
        ))}
      </div>
      {lastCheckIn ? (
        <p className="mt-4 rounded-xl bg-emerald-50 p-3 text-xs leading-5 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200">
          最近进度：{lastCheckIn.note}
        </p>
      ) : null}
      <div className="mt-4 grid gap-4">
        <div className="grid gap-4 md:grid-cols-2">
          <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
            状态
            <select
              className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
              value={draft.status}
              onChange={(event) => updateTaskDraft(task.id, { status: event.target.value as TaskStatus })}
            >
              <option value="todo">todo</option>
              <option value="doing">doing</option>
              <option value="blocked">blocked</option>
              <option value="done">done</option>
            </select>
          </label>
          <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
            实际耗时
            <input
              className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
              min="0"
              step="0.5"
              type="number"
              value={draft.actual_hours}
              onChange={(event) => updateTaskDraft(task.id, { actual_hours: event.target.value })}
            />
          </label>
        </div>
        <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
          Check-in
          <textarea
            className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all min-h-24 resize-y px-3 py-2 text-sm leading-6 text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
            placeholder="今天推进了什么、卡在哪里、下一步做什么"
            value={draft.check_in}
            onChange={(event) => updateTaskDraft(task.id, { check_in: event.target.value })}
          />
        </label>
        <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
          完成备注
          <textarea
            className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all min-h-24 resize-y px-3 py-2 text-sm leading-6 text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
            placeholder="完成范围、关键结论、可复用亮点"
            value={draft.completion_notes}
            onChange={(event) => updateTaskDraft(task.id, { completion_notes: event.target.value })}
          />
        </label>
        <label className="grid gap-4 text-xs font-medium text-zinc-700 dark:text-zinc-300">
          产物链接
          <input
            className="bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all px-3 py-2 text-sm text-zinc-900 dark:text-zinc-100 md:px-4 md:py-3"
            placeholder="https://github.com/... 或文档链接"
            value={draft.artifact_url}
            onChange={(event) => updateTaskDraft(task.id, { artifact_url: event.target.value })}
          />
        </label>
        <div className="flex flex-wrap gap-4">
          <ActionButton disabled={isBusy} onClick={() => saveTaskProgress(task)} variant="secondary">
            保存进度
          </ActionButton>
          <ActionButton disabled={isBusy} onClick={() => saveTaskProgress(task, { complete: true, createEvidence: true })}>
            完成并生成证据
          </ActionButton>
        </div>
      </div>
    </article>
  );
}

function EvidenceItem({ item }: { item: CareerEvidence }) {
  const artifactLinks = Object.entries(item.artifacts).filter(([, value]) => value);

  return (
    <article className="rounded-xl bg-zinc-50 p-4 dark:bg-zinc-800">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <h3 className="font-semibold text-zinc-900 dark:text-zinc-100">{item.title}</h3>
        <Badge text={item.evidence_strength} tone={item.evidence_strength === "strong" ? "good" : item.evidence_strength === "medium" ? "warn" : "neutral"} />
      </div>
      <div className="mt-4 flex flex-wrap gap-4">
        <Badge text={item.type} />
        {item.source_task_id ? <Badge text={item.source_task_id} /> : null}
        {item.verified ? <Badge text="verified" tone="good" /> : <Badge text="needs link" tone="warn" />}
      </div>
      <p className="mt-4 text-sm leading-6 text-zinc-600 dark:text-zinc-400">
        {item.resume_bullets[0] ?? "No bullet generated."}
      </p>
      <div className="mt-4 flex flex-wrap gap-4">
        {item.skills.map((skill) => (
          <Badge key={skill} text={skill} />
        ))}
      </div>
      {artifactLinks.length > 0 ? (
        <div className="mt-4 grid gap-4">
          {artifactLinks.map(([label, value]) => (
            <a
              key={`${item.id}-${label}`}
              className="break-words text-xs leading-5 text-emerald-800 underline decoration-emerald-300 underline-offset-4 dark:text-emerald-200"
              href={value}
              rel="noreferrer"
              target="_blank"
            >
              {label}: {value}
            </a>
          ))}
        </div>
      ) : null}
    </article>
  );
}

function Badge({ text, tone = "neutral" }: { text: string; tone?: "neutral" | "good" | "warn" | "bad" }) {
  const color =
    tone === "good"
      ? "bg-emerald-50 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200"
      : tone === "warn"
        ? "bg-amber-50 text-amber-800 dark:bg-amber-950 dark:text-amber-200"
        : tone === "bad"
          ? "bg-red-50 text-red-800 dark:bg-red-950 dark:text-red-200"
          : "bg-zinc-100 text-zinc-600 dark:bg-zinc-700 dark:text-zinc-200";
  return <span className={`rounded-xl px-3 py-2 text-xs ${color}`}>{text}</span>;
}
