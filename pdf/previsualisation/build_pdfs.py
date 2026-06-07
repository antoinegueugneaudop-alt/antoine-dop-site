from pathlib import Path
import html
import shutil

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import ImageReader
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "pdf" / "previsualisation"
OUT_DIR = ROOT / "public" / "downloads"
LOCAL_DOWNLOADS_DIR = ROOT / "downloads"

PAGE_W, PAGE_H = landscape(A4)
M = 46
INK = HexColor("#111111")
MUTED = HexColor("#5f5f5f")
SOFT = HexColor("#9a9a9a")
LINE = HexColor("#dedbd5")
BG = HexColor("#fbfaf8")


ASSETS = {
    "case01": "assets/visual_preparation/case01-time-lapse-location-validation/_thumbs/06-visualized-timelapse-proposal.jpg",
    "case02_before": "assets/visual_preparation/case02-fictional-architecture-real-city/01-real-city-context.jpg",
    "case02_after": "assets/visual_preparation/case02-fictional-architecture-real-city/02-visualized-fictional-landmark-wide.jpg",
    "case02": "assets/visual_preparation/02-fictional-architecture-real-city.jpg",
    "case03": "assets/visual_preparation/03-windshield-vfx-driving-sequence.jpg",
    "case04": "assets/visual_preparation/04-rapid-action-visualization.jpg",
    "case05": "assets/visual_preparation/case05-meduse-pablo-live-action-integration/05-meduse-pablo-card-cover-2-1.jpg",
    "case06": "assets/visual_preparation/case06-invisible-ai-production-solution/06-animal-design-approved-muddy-dog-2-1.jpg",
    "case07": "assets/visual_preparation/case07-set-transformation-previsualization/07-set-transformation-card-cover-2-1.jpg",
    "case08": "assets/visual_preparation/case08-super8-1977-period-texture/08-super8-1977-film-gate-study-06.jpg",
}


DOCS = {
    "fr": {
        "filename": "Previsualisation_Supervision_IA_Production_FR.pdf",
        "html": "source-fr.html",
        "title": "Prévisualisation & supervision IA",
        "subtitle": "Un outil de décision pour productions cinéma, séries, télévision et plateformes.",
        "promise": ["Voir avant d’engager.", "Comparer avant de dépenser.", "Valider avant de tourner."],
        "p2_title": "Le gain production",
        "p2_text": "La valeur n’est pas l’image seule. C’est la décision qu’elle permet de prendre avant les dépenses lourdes.",
        "p2_statement": ["Voir plus tôt.", "Décider plus vite.", "Fabriquer plus juste."],
        "p2_cards": [
            ("01", "Moins de flou", "Décors, mouvements, VFX et contraintes deviennent visibles avant le tournage."),
            ("02", "Moins d’allers-retours", "Une référence partagée circule entre réalisation, production, image, décoration et VFX."),
            ("03", "Coûts cachés réduits", "Arbitrer plus tôt ce qui doit être tourné, simplifié, sécurisé, préparé en VFX ou abandonné."),
        ],
        "p3_title": "Une interface de décision",
        "p3_subtitle": "Des contraintes réelles vers des options validables.",
        "p3_flow": ["INTENTION", "RÉEL", "OPTION VISUELLE", "VALIDATION", "FABRICATION"],
        "p3_text": "Chaque cas part d’un élément concret : lieu réel, contrainte de tournage, intention de mise en scène, besoin VFX ou problème de production. La prévisualisation transforme ce point de départ en options visuelles lisibles, comparables et transmissibles.",
        "p4_title": "Applications concrètes en production",
        "p4_subtitle": "Des images de prévisualisation conçues pour sécuriser des décisions de production, pas pour faire une démonstration technologique.",
        "apps": [
            ("01", "Validation décor", "Confirmer lieu, temporalité, lumière et besoins VFX.", "case01"),
            ("02", "Intégration architecturale", "Tester une architecture fictive dans un lieu réel.", "case02"),
            ("03", "Pare-brise VFX / conduite", "Aligner plateau, studio, reflets, vitesse, HUD et post-production.", "case03"),
            ("04", "IA invisible / économie de moyens", "Préparer un élément secondaire sans alourdir le tournage.", "case06"),
            ("05", "Dessin → live-action", "Passer d’une intention graphique à un plan exploitable.", "case05"),
            ("06", "Storyboard opérationnel", "Transformer un découpage en référence partagée.", "case04"),
            ("07", "Transformation décor", "Valider continuité personnage, décor et VFX.", "case07"),
            ("08", "Super 8 / 1977", "Créer une texture époque exploitable.", "case08"),
        ],
        "p5_title": "Superviseur du Développement Visuel Assisté par IA",
        "p5_subtitle": "Une interface de production entre réalisation, image, décoration et VFX.",
        "p5_text": "Certaines décisions coûtent cher lorsqu’elles sont prises trop tard : décors, VFX, animaux, enfants, véhicules, séquences d’action, météo et logistique de tournage.\n\nLe rôle consiste à utiliser l’intelligence artificielle comme un outil de préproduction afin de permettre aux réalisateurs et aux productions de visualiser, tester et valider différentes solutions avant d’engager les moyens de fabrication.",
        "p5_blocks": [
            ("Réduire les risques", "Identifier plus tôt les sujets production, VFX et logistique."),
            ("Valider plus vite", "Donner à la réalisation et à la production une référence claire avant engagement."),
            ("Comparer les options", "Tester plusieurs solutions avant d’ouvrir les dépenses lourdes."),
            ("Aligner les équipes", "Créer un langage visuel commun entre réalisation, production, image, décoration et VFX."),
        ],
        "p5_end": ["L’objectif n’est pas de remplacer les équipes.", "L’objectif est de prendre de meilleures décisions, plus tôt."],
        "p6_title": "Trois décisions de production sécurisées avant tournage",
        "p6_subtitle": "Des images utiles pour valider, budgéter et transmettre.",
        "examples": [
            ("01", "Valider un décor", "Montrer le potentiel d’un lieu, sa lumière, sa temporalité et ses contraintes VFX avant engagement.", "case01"),
            ("02", "Aligner un plan VFX", "Partager une cible claire entre réalisation, image, studio, plateau et post-production.", "case02_after"),
            ("03", "Réduire une logistique", "Remplacer une contrainte lourde par un élément discret, contrôlé et préparé pour l’intégration live-action.", "case06"),
        ],
        "p7_title": "Comment les productions peuvent l’utiliser",
        "p7_subtitle": "Une couche de préparation flexible, d’un problème visuel ponctuel à un accompagnement de préproduction complet.",
        "formats": [
            ("01", "Sprint de décision visuelle", "1 à 3 jours", "Pour un décor, une question VFX ou une incertitude de production.", "Images clés, options visuelles et notes concises de tournage / VFX.", "Arbitrer tôt, confirmer un repérage ou valider une intention avec réalisation et production."),
            ("02", "Dossier de préparation séquence", "Environ une semaine", "Pour une scène complexe, une action, un dispositif VFX ou une décision coûteuse.", "Storyboard, tests visuels, comparaison d’options, notes par poste et proposition de méthode de tournage.", "Aligner réalisation, production, image, décoration et VFX avant le tournage."),
            ("03", "Interface de préproduction intégrée", "Préparation longue", "Pour un long métrage, une série ou plusieurs séquences à préparer.", "Bible visuelle partagée, décisions visuelles récurrentes, alignement VFX, notes production et coordination entre départements.", "Maintenir l’intention artistique, les contraintes de production et les besoins de post-production alignés jusqu’au tournage."),
        ],
        "contact_role": ["Directeur de la Photographie", "Superviseur du Développement Visuel Assisté par IA"],
    },
    "en": {
        "filename": "Visual_Preparation_AI_Supervision_Production_EN.pdf",
        "html": "source-en.html",
        "title": "Visual Preparation & AI Supervision",
        "subtitle": "A decision tool for film, series, television and platform productions.",
        "promise": ["See before committing.", "Compare before spending.", "Validate before shooting."],
        "p2_title": "Production gain",
        "p2_text": "The value is not the image alone. It is the decision the image makes possible before heavy spending begins.",
        "p2_statement": ["See earlier.", "Decide faster.", "Build more precisely."],
        "p2_cards": [
            ("01", "Less uncertainty", "Locations, movements, VFX and constraints become visible before the shoot."),
            ("02", "Fewer back-and-forths", "One shared reference circulates between direction, production, cinematography, art department, locations and VFX."),
            ("03", "Lower hidden costs", "Arbitrate earlier what should be shot, simplified, secured, prepared in VFX or abandoned."),
        ],
        "p3_title": "A decision interface",
        "p3_subtitle": "From real constraints to validatable options.",
        "p3_flow": ["INTENT", "REALITY", "VISUAL OPTION", "VALIDATION", "SHOOT / VFX"],
        "p3_text": "Each case starts from a concrete element: a real location, a shooting constraint, a directing intention, a VFX need or a production problem. Visual preparation turns that starting point into useful, comparable and shareable images.",
        "p4_title": "Practical production uses",
        "p4_subtitle": "Visual preparation images designed to secure decisions, not to demonstrate technology.",
        "apps": [
            ("01", "Location validation", "Confirm location, time-of-day, light and VFX needs.", "case01"),
            ("02", "Architectural integration", "Test fictional architecture inside a real location.", "case02"),
            ("03", "Windshield VFX / driving", "Align set, studio, reflections, speed, HUD and post-production.", "case03"),
            ("04", "Invisible AI / reduced logistics", "Prepare a discreet secondary element without weighing down the shoot.", "case06"),
            ("05", "Drawing → live-action", "Move from graphic intention to an exploitable shot.", "case05"),
            ("06", "Operational storyboard", "Turn an action breakdown into a shared reference.", "case04"),
            ("07", "Set transformation", "Validate character, environment continuity and VFX.", "case07"),
            ("08", "Super 8 / 1977", "Create a usable period texture direction.", "case08"),
        ],
        "p5_title": "AI-Assisted Visual Development Supervisor",
        "p5_subtitle": "A production interface between direction, cinematography, art department and VFX.",
        "p5_text": "Some decisions become expensive when they are made too late: locations, VFX, animals, children, vehicles, action sequences, weather and shooting logistics.\n\nThe role is to use AI as a preproduction tool to help directors and productions visualize, test and validate options before committing production resources.",
        "p5_blocks": [
            ("Reduce risk", "Identify production, VFX and logistics issues earlier."),
            ("Validate faster", "Give direction and production a clear reference before committing resources."),
            ("Compare options", "Test several solutions before opening heavy spending."),
            ("Align departments", "Create a shared visual language between direction, production, cinematography, art department and VFX."),
        ],
        "p5_end": ["The goal is not to replace teams.", "The goal is to make better decisions, earlier."],
        "p6_title": "Three production decisions secured before shooting",
        "p6_subtitle": "Useful images to validate, budget and share.",
        "examples": [
            ("01", "Validate a location", "Show location potential, light, time-of-day and VFX constraints before commitment.", "case01"),
            ("02", "Align a VFX shot", "Share a clear target between direction, cinematography, studio, set and post-production.", "case02_after"),
            ("03", "Reduce logistics", "Replace a heavy constraint with a discreet, controlled element prepared for live-action integration.", "case06"),
        ],
        "p7_title": "How productions can use this",
        "p7_subtitle": "A flexible preparation layer, from one visual problem to full preproduction support.",
        "formats": [
            ("01", "Visual Decision Sprint", "1 to 3 days", "For one location, one VFX question or one production uncertainty.", "Key frames, visual options and concise shooting / VFX notes.", "Early arbitration before spending, scouting confirmation or producer/director validation."),
            ("02", "Sequence Preparation Pack", "Around one week", "For a complex scene, action beat, VFX setup or costly production decision.", "Storyboard, visual tests, options comparison, department notes and recommended shooting approach.", "Aligning direction, production, cinematography, art department and VFX before the shoot."),
            ("03", "Embedded Preproduction Interface", "Longer prep", "For a feature film, series or multi-sequence preparation period.", "Shared visual bible, recurring visual decisions, VFX alignment, production-facing notes and department coordination.", "Keeping creative intent, production constraints and post-production needs aligned until the shoot."),
        ],
        "contact_role": ["Director of Photography", "AI-Assisted Visual Development Supervisor"],
    },
}


def rel(path):
    return ROOT / path


def wrap_text(c, text, max_width, font="Helvetica", size=12):
    lines = []
    for para in text.split("\n"):
        if not para:
            lines.append("")
            continue
        words = para.split()
        current = ""
        for word in words:
            test = (current + " " + word).strip()
            if stringWidth(test, font, size) <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def text_block(c, text, x, y, w, size=12, leading=16, font="Helvetica", color=MUTED):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap_text(c, text, w, font, size):
        if line:
            c.drawString(x, y, line)
        y -= leading
    return y


def text_block_limited(c, text, x, y, w, size=12, leading=16, max_lines=3, font="Helvetica", color=MUTED):
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap_text(c, text, w, font, size)[:max_lines]
    for line in lines:
        if line:
            c.drawString(x, y, line)
        y -= leading
    return y


def label(c, text, x, y):
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(SOFT)
    c.drawString(x, y, text.upper())


def title(c, text, x, y, size=36, w=520):
    c.setFont("Times-Roman", size)
    c.setFillColor(INK)
    for line in wrap_text(c, text, w, "Times-Roman", size):
        c.drawString(x, y, line)
        y -= size * 1.02
    return y


def rule(c, y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.line(M, y, PAGE_W - M, y)


def draw_image(c, asset_key, x, y, w, h):
    path = rel(ASSETS[asset_key])
    if not path.exists():
        c.setFillColor(HexColor("#eeeeee"))
        c.rect(x, y, w, h, fill=1, stroke=0)
        return
    with Image.open(path) as im:
        iw, ih = im.size
    image_ratio = iw / ih
    box_ratio = w / h
    if image_ratio > box_ratio:
        draw_h = h
        draw_w = h * image_ratio
        dx = x - (draw_w - w) / 2
        dy = y
    else:
        draw_w = w
        draw_h = w / image_ratio
        dx = x
        dy = y - (draw_h - h) / 2
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0)
    c.drawImage(ImageReader(str(path)), dx, dy, draw_w, draw_h, preserveAspectRatio=False, mask="auto")
    c.restoreState()
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.rect(x, y, w, h, stroke=1, fill=0)


def footer(c, page_no):
    c.setFont("Helvetica", 7.5)
    c.setFillColor(SOFT)
    c.drawString(M, 24, "ANTOINE GUEUGNEAU — AI VISUAL PREPARATION")
    c.drawRightString(PAGE_W - M, 24, f"{page_no:02d} / 07")


def page_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def render_cover(c, d):
    page_bg(c)
    label(c, "AI VISUAL PREPARATION", M, PAGE_H - 58)
    title(c, d["title"], M, PAGE_H - 104, 42, 430)
    text_block(c, d["subtitle"], PAGE_W - 330, PAGE_H - 116, 284, 13.5, 18, "Helvetica", MUTED)
    y = 398
    c.setFont("Times-Roman", 27)
    c.setFillColor(INK)
    for line in d["promise"]:
        c.drawString(M, y, line)
        y -= 31
    draw_image(c, "case01", M, 44, PAGE_W - 2 * M, 270)
    footer(c, 1)
    c.showPage()


def render_gain(c, d):
    page_bg(c)
    label(c, "PRODUCTION", M, PAGE_H - 62)
    title(c, d["p2_title"], M, PAGE_H - 110, 38, 430)
    text_block(c, d["p2_text"], M, PAGE_H - 172, 430, 13, 18)
    y = PAGE_H - 272
    c.setFont("Times-Roman", 35)
    c.setFillColor(INK)
    for line in d["p2_statement"]:
        c.drawString(M, y, line)
        y -= 38
    y0 = PAGE_H - 210
    card_w = 210
    for i, (num, head, body) in enumerate(d["p2_cards"]):
        x = PAGE_W - M - (3 - i) * card_w - (2 - i) * 18
        c.setStrokeColor(LINE)
        c.rect(x, y0 - 180, card_w, 180, stroke=1, fill=0)
        label(c, num, x + 18, y0 - 34)
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(INK)
        c.drawString(x + 18, y0 - 68, head)
        text_block(c, body, x + 18, y0 - 98, card_w - 36, 11, 15.5)
    footer(c, 2)
    c.showPage()


def draw_flow(c, items, x, y, total_w):
    box_gap = 8
    box_w = (total_w - box_gap * (len(items) - 1)) / len(items)
    for i, item in enumerate(items):
        bx = x + i * (box_w + box_gap)
        c.setStrokeColor(LINE)
        c.roundRect(bx, y, box_w, 38, 6, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", 8.2)
        c.setFillColor(INK)
        c.drawCentredString(bx + box_w / 2, y + 15, item)


def render_interface(c, d):
    page_bg(c)
    label(c, "DECISION INTERFACE", M, PAGE_H - 62)
    title(c, d["p3_title"], M, PAGE_H - 108, 38, 420)
    text_block(c, d["p3_subtitle"], M, PAGE_H - 158, 300, 13, 17, "Helvetica", MUTED)
    draw_flow(c, d["p3_flow"], M, PAGE_H - 228, PAGE_W - 2 * M)
    text_block(c, d["p3_text"], M, PAGE_H - 288, 356, 12, 17)
    draw_image(c, "case02_before", 424, 220, 170, 102)
    label(c, "REALITY", 424, 334)
    draw_image(c, "case02_after", 610, 70, PAGE_W - 656, 242)
    label(c, "VALIDATED OPTION", 610, 334)
    footer(c, 3)
    c.showPage()


def render_apps(c, d):
    page_bg(c)
    label(c, "APPLICATIONS", M, PAGE_H - 62)
    title(c, d["p4_title"], M, PAGE_H - 108, 38, 520)
    text_block(c, d["p4_subtitle"], M, PAGE_H - 162, 560, 12, 17)
    featured = d["apps"][:4]
    listed = d["apps"][4:]
    card_w = (PAGE_W - 2 * M - 42) / 4
    top = PAGE_H - 246
    for i, (num, name, body, asset) in enumerate(featured):
        x = M + i * (card_w + 14)
        draw_image(c, asset, x, top - 136, card_w, 136)
        label(c, num, x, top - 158)
        c.setFont("Helvetica-Bold", 10.8)
        c.setFillColor(INK)
        c.drawString(x + 28, top - 158, name)
    y = 126
    col_w = (PAGE_W - 2 * M - 26) / 2
    for i, (num, name, body, asset) in enumerate(listed):
        x = M + (i % 2) * (col_w + 26)
        yy = y - (i // 2) * 42
        c.setStrokeColor(LINE)
        c.line(x, yy + 20, x + col_w, yy + 20)
        label(c, num, x, yy)
        c.setFont("Helvetica-Bold", 11.5)
        c.setFillColor(INK)
        c.drawString(x + 34, yy, name)
        text_block_limited(c, body, x + 34, yy - 17, col_w - 34, 9.4, 12, 1)
    footer(c, 4)
    c.showPage()


def render_supervisor(c, d):
    page_bg(c)
    label(c, "SUPERVISION", M, PAGE_H - 62)
    title(c, d["p5_title"], M, PAGE_H - 108, 34, 650)
    text_block(c, d["p5_subtitle"], M, PAGE_H - 154, 560, 13, 18)
    text_block(c, d["p5_text"], M, PAGE_H - 216, 385, 11.5, 16.5)
    card_w = 164
    start_x = PAGE_W - M - card_w * 2 - 20
    start_y = PAGE_H - 220
    for i, (head, body) in enumerate(d["p5_blocks"]):
        x = start_x + (i % 2) * (card_w + 20)
        y = start_y - (i // 2) * 118
        c.setStrokeColor(LINE)
        c.roundRect(x, y - 82, card_w, 82, 7, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(INK)
        c.drawString(x + 14, y - 25, head.upper())
        text_block(c, body, x + 14, y - 48, card_w - 28, 9.5, 12.5)
    c.setFont("Times-Roman", 23)
    c.setFillColor(INK)
    y = 96
    for line in d["p5_end"]:
        c.drawString(M, y, line)
        y -= 27
    footer(c, 5)
    c.showPage()


def render_examples(c, d):
    page_bg(c)
    label(c, "EXAMPLES", M, PAGE_H - 62)
    title(c, d["p6_title"], M, PAGE_H - 108, 31, 760)
    text_block(c, d["p6_subtitle"], M, PAGE_H - 158, 520, 12, 17)
    top = PAGE_H - 218
    card_w = (PAGE_W - 2 * M - 42) / 3
    for i, (num, head, body, asset) in enumerate(d["examples"]):
        x = M + i * (card_w + 19)
        draw_image(c, asset, x, top - 150, card_w, 150)
        label(c, num, x, top - 174)
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(INK)
        c.drawString(x + 32, top - 174, head)
        text_block(c, body, x, top - 204, card_w, 10.3, 14)
    footer(c, 6)
    c.showPage()


def render_contact(c, d):
    page_bg(c)
    label(c, "MISSION", M, PAGE_H - 62)
    title(c, d["p7_title"], M, PAGE_H - 108, 38, 620)
    text_block(c, d["p7_subtitle"], M, PAGE_H - 160, 620, 12, 17)
    card_w = (PAGE_W - 2 * M - 38) / 3
    y = PAGE_H - 218
    for i, (num, head, duration, intro, deliverables, best_for) in enumerate(d["formats"]):
        x = M + i * (card_w + 19)
        c.setStrokeColor(LINE)
        c.roundRect(x, y - 186, card_w, 186, 8, stroke=1, fill=0)
        label(c, num, x + 18, y - 34)
        c.setFont("Helvetica-Bold", 11.8)
        c.setFillColor(INK)
        text_block_limited(c, head, x + 18, y - 66, card_w - 36, 11.5, 14, 2, "Helvetica-Bold", INK)
        c.setFont("Helvetica", 10.5)
        c.setFillColor(MUTED)
        c.drawString(x + 18, y - 96, duration)
        text_block_limited(c, intro, x + 18, y - 120, card_w - 36, 9.1, 11.2, 2)
        label(c, "Deliverables", x + 18, y - 158)
        text_block_limited(c, deliverables, x + 18, y - 174, card_w - 36, 8.2, 10.2, 1)
    c.setStrokeColor(LINE)
    c.line(M, 122, PAGE_W - M, 122)
    c.setFont("Helvetica-Bold", 17)
    c.setFillColor(INK)
    c.drawString(M, 90, "ANTOINE GUEUGNEAU")
    c.setFont("Helvetica", 11.5)
    c.setFillColor(MUTED)
    c.drawString(M, 68, d["contact_role"][0])
    c.drawString(M, 50, d["contact_role"][1])
    c.setFillColor(INK)
    c.drawRightString(PAGE_W - M, 68, "+33 6 80 62 71 26")
    c.drawRightString(PAGE_W - M, 50, "antoinegueugneau.dop@gmail.com")
    footer(c, 7)
    c.showPage()


def build_pdf(lang, data):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / data["filename"]
    c = canvas.Canvas(str(out), pagesize=landscape(A4))
    c.setTitle(data["title"])
    render_cover(c, data)
    render_gain(c, data)
    render_interface(c, data)
    render_apps(c, data)
    render_supervisor(c, data)
    render_examples(c, data)
    render_contact(c, data)
    c.save()
    return out


def write_sources():
    SRC_DIR.mkdir(parents=True, exist_ok=True)
    css = """@page { size: A4 landscape; margin: 0; }
body { margin: 0; background: #fbfaf8; color: #111; font-family: Helvetica, Arial, sans-serif; }
.page { width: 297mm; height: 210mm; box-sizing: border-box; padding: 16mm; page-break-after: always; }
h1, .statement { font-family: Georgia, 'Times New Roman', serif; font-weight: 400; letter-spacing: -0.04em; }
.kicker, .label { color: #9a9a9a; text-transform: uppercase; font-weight: 700; letter-spacing: .14em; font-size: 8.5pt; }
p { color: #5f5f5f; line-height: 1.45; }
.grid { display: grid; gap: 8mm; }
.two { grid-template-columns: 1fr 1fr; }
.three { grid-template-columns: repeat(3, 1fr); }
.four { grid-template-columns: repeat(4, 1fr); }
img { width: 100%; height: 100%; object-fit: cover; border: 0.5pt solid #dedbd5; }
"""
    (SRC_DIR / "previsualisation.css").write_text(css, encoding="utf-8")
    for lang, d in DOCS.items():
        parts = [
            "<!doctype html>",
            f"<html lang=\"{lang}\"><head><meta charset=\"utf-8\"><title>{html.escape(d['title'])}</title><link rel=\"stylesheet\" href=\"previsualisation.css\"></head><body>",
            f"<section class=\"page\"><div class=\"kicker\">AI Visual Preparation</div><h1>{html.escape(d['title'])}</h1><p>{html.escape(d['subtitle'])}</p><div class=\"statement\">{'<br>'.join(html.escape(x) for x in d['promise'])}</div><img src=\"../../{ASSETS['case01']}\" alt=\"\"></section>",
            f"<section class=\"page\"><div class=\"kicker\">Production</div><h1>{html.escape(d['p2_title'])}</h1><p>{html.escape(d['p2_text'])}</p></section>",
            f"<section class=\"page\"><div class=\"kicker\">Decision interface</div><h1>{html.escape(d['p3_title'])}</h1><p>{html.escape(d['p3_text'])}</p></section>",
            f"<section class=\"page\"><div class=\"kicker\">Applications</div><h1>{html.escape(d['p4_title'])}</h1></section>",
            f"<section class=\"page\"><div class=\"kicker\">Supervision</div><h1>{html.escape(d['p5_title'])}</h1><p>{html.escape(d['p5_text'])}</p></section>",
            f"<section class=\"page\"><div class=\"kicker\">Examples</div><h1>{html.escape(d['p6_title'])}</h1></section>",
            f"<section class=\"page\"><div class=\"kicker\">Mission</div><h1>{html.escape(d['p7_title'])}</h1></section>",
            "</body></html>",
        ]
        (SRC_DIR / d["html"]).write_text("\n".join(parts), encoding="utf-8")


def main():
    write_sources()
    LOCAL_DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    for lang, data in DOCS.items():
        out = build_pdf(lang, data)
        shutil.copy2(out, LOCAL_DOWNLOADS_DIR / out.name)
        print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
