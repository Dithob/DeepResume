declare module "lucide-react" {
  import type { ComponentType, SVGProps } from "react";

  export type LucideIcon = ComponentType<SVGProps<SVGSVGElement> & { size?: number | string }>;

  export const BookOpenCheck: LucideIcon;
  export const BriefcaseBusiness: LucideIcon;
  export const ClipboardList: LucideIcon;
  export const Database: LucideIcon;
  export const Gauge: LucideIcon;
  export const UploadCloud: LucideIcon;
}
