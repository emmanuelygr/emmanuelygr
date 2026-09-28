from pathlib import Path

OUTPUT = Path("avatar.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg"
     width="420"
     height="420"
     viewBox="0 0 420 420"
     role="img"
     aria-label="Anonymous cybersecurity terminal avatar">

  <rect width="420" height="420" rx="14" fill="#0d1117"/>

  <!-- terminal window -->
  <rect x="16" y="16" width="388" height="388"
        rx="12"
        fill="#010409"
        stroke="#30363d"
        stroke-width="2"/>

  <!-- terminal header -->
  <rect x="16" y="16" width="388" height="42"
        rx="12"
        fill="#161b22"/>

  <circle cx="39" cy="37" r="5" fill="#8b949e"/>
  <circle cx="57" cy="37" r="5" fill="#8b949e"/>
  <circle cx="75" cy="37" r="5" fill="#8b949e"/>

  <text x="210" y="41"
        text-anchor="middle"
        font-family="monospace"
        font-size="13"
        fill="#8b949e">
    emmanuel@github: ~
  </text>

  <!-- terminal prompt -->
  <text x="38" y="88"
        font-family="monospace"
        font-size="15"
        fill="#58a6ff">
    $ whoami
  </text>

  <text x="38" y="112"
        font-family="monospace"
        font-size="14"
        fill="#8b949e">
    unknown_user
  </text>

  <!-- anonymous face -->
  <g class="face"
     fill="none"
     stroke="#c9d1d9"
     stroke-width="6"
     stroke-linecap="round"
     stroke-linejoin="round">

    <path d="
      M210 145
      C160 145 128 177 128 225
      C128 274 160 306 210 306
      C260 306 292 274 292 225
      C292 177 260 145 210 145
      Z"/>

    <!-- shoulders -->
    <path d="
      M128 306
      C92 318 67 340 57 378"/>

    <path d="
      M292 306
      C328 318 353 340 363 378"/>

    <path d="
      M128 306
      C153 326 177 335 210 335
      C243 335 267 326 292 306"/>
  </g>

  <!-- question mark -->
  <text x="210"
        y="258"
        text-anchor="middle"
        font-family="monospace"
        font-size="92"
        font-weight="bold"
        fill="#58a6ff">
    ?
  </text>

  <!-- security status -->
  <text x="38" y="372"
        font-family="monospace"
        font-size="13"
        fill="#8b949e">
    [ SECURITY MODE ]
  </text>

  <!-- cursor -->
  <rect x="194" y="372" width="8" height="13" fill="#58a6ff">
    <animate
      attributeName="opacity"
      values="1;0;1"
      dur="1s"
      repeatCount="indefinite"/>
  </rect>

  <!-- drawing animation -->
  <style>
    .face {
      stroke-dasharray: 1100;
      stroke-dashoffset: 1100;
      animation: draw 2.5s ease-out forwards;
    }

    @keyframes draw {
      to {
        stroke-dashoffset: 0;
      }
    }
  </style>

</svg>
"""

OUTPUT.write_text(svg, encoding="utf-8")
print(f"Created {OUTPUT}")
