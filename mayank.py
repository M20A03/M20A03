#!/usr/bin/env python3
"""
Mayank Raj — Engineering Architecture & Systems Manifest
Repository: M20A03/M20A03
Identity: Full-Stack Systems Architect & AI Researcher
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json

@dataclass(frozen=True)
class Deployment:
    name: str
    category: str
    stack: str
    live_url: str
    status: str = "PRODUCTION_ACTIVE"

@dataclass
class Engineer:
    handle: str = "M20A03"
    name: str = "Mayank Raj"
    role: str = "Full-Stack Systems Architect & AI Researcher"
    institution: str = "Christ University, Bengaluru"
    location: str = "Bengaluru, India"
    website: str = "https://www.mayankraj.me"
    linkedin: str = "https://www.linkedin.com/in/mayank-raj-gupta"
    email: str = "mayankrajgupta01@gmail.com"

    # Core Research Systems
    flagship_ai_system: str = "Praxirence (Ambient Clinical Intelligence)"
    ai_specialization: List[str] = field(default_factory=lambda: [
        "Acoustic Speech Recognition (Whisper ASR)",
        "Clinical LLM Inference (Mistral-7B / BioMistral)",
        "Zero-Trust Encryption (AES-256-GCM / In-Memory Shredding)",
        "Computer Vision & Spectral Analysis (OpenCV, PyTorch)"
    ])

    # Tech Stack (Primary: Python, Full-Stack, Java) - Strictly Zero C/C++
    technical_stack: Dict[str, List[str]] = field(default_factory=lambda: {
        "core_languages": ["Python", "Java (Swing, JSP)", "TypeScript", "JavaScript", "SQL"],
        "ai_and_ml": ["PyTorch", "Whisper ASR", "Mistral-7B", "OpenCV", "NumPy", "Pandas", "Scikit-Learn"],
        "frontend_engineering": ["Next.js 15", "React 19", "Tailwind CSS", "Angular", "Framer Motion", "HTML5", "CSS3"],
        "backend_and_cloud": ["Python FastAPI", "Java Enterprise", "Docker", "PostgreSQL", "Firebase", "Vercel"],
        "mobile_and_realtime": ["React Native", "Expo Native", "Android", "WebRTC"]
    })

    deployments: List[Deployment] = field(default_factory=lambda: [
        Deployment("Praxirence", "Ambient Clinical AI", "Expo Native / FastAPI / Whisper / Mistral-7B", "https://github.com/M20A03/Praxirence"),
        Deployment("Credex", "FinTech / AI Risk Audit", "Next.js 15 / React 19 / Claude AI", "https://credex-sand.vercel.app/"),
        Deployment("Portfolio 2026", "Spatial Web", "Next.js 15 / React 19 / Radix UI", "https://portfolio-alpha-kohl-lqt3tnm7tp.vercel.app/"),
        Deployment("StudyArchive", "EdTech Platform", "Angular 21 (SSR) / TypeScript / Firebase", "https://straw-hats-7795d.web.app/"),
        Deployment("Nexus-Scholar", "University Hub", "React 18 / Python FastAPI / Gemini AI", "https://nexus-scholar-huhs.vercel.app/"),
        Deployment("Roshan Enterprises", "B2B/B2C Commerce", "React 18 / Vite / Firebase Firestore", "https://e-commerce-roshan-enterprises-dhn.web.app/"),
        Deployment("Fintech Neobank", "Neobank Dashboard", "Vanilla ES6+ / 3D Gyroscope Physics", "https://fintech-six-pi.vercel.app/"),
        Deployment("Sakthi Dental Clinic", "Medical Scheduling", "React 18 / Vite / Clinical UX", "https://sakthi-dental-clinic-rust.vercel.app/")
    ])

    def summarize(self) -> str:
        lines = [
            f"=== {self.name} [{self.handle}] ===",
            f"Role: {self.role}",
            f"Focus: {self.flagship_ai_system}",
            f"Primary Language: Python",
            f"Active Deployments: {len(self.deployments)} Verified Systems",
            f"Website: {self.website}",
            f"LinkedIn: {self.linkedin}",
            "==================================="
        ]
        return "\n".join(lines)

def main() -> None:
    engineer = Engineer()
    print(engineer.summarize())

if __name__ == "__main__":
    main()
