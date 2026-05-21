import re

html_path = 'championship/syllabus-videos.html'

with open(html_path, 'r') as f:
    content = f.read()

# Extract videos from the current HTML
videos = []
matches = re.finditer(r'<a href="([^"]+)".*?class="video-card">\s*<span class="video-no">(\d+)</span>\s*<span class="video-name">([^<]+)</span>', content, re.DOTALL)

for m in matches:
    url = m.group(1)
    no = int(m.group(2))
    name = m.group(3).strip()
    
    # Extract video ID
    # URLs are like https://youtu.be/ID or https://youtube.com/shorts/ID
    if 'youtu.be/' in url:
        vid_id = url.split('youtu.be/')[1].split('?')[0]
    elif 'shorts/' in url:
        vid_id = url.split('shorts/')[1].split('?')[0]
    else:
        vid_id = url.split('/')[-1]
        
    videos.append({
        'no': no,
        'name': name,
        'url': url,
        'id': vid_id
    })

videos.sort(key=lambda x: x['no'])

# Generate the new HTML
new_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <base href="../" />
  <title>Syllabus and Guidelines (Videos) | West Bengal Yoga Association</title>
  <link rel="stylesheet" href="assets/css/styles.css" />
  <link rel="stylesheet" href="assets/css/members.css" />
  <style>
    .videos-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 24px;
      margin-top: 32px;
    }
    .video-card {
      background: rgba(255, 255, 255, 0.8);
      border: 1px solid rgba(22, 101, 52, 0.1);
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transition: all 0.3s ease;
      text-decoration: none;
      color: var(--color-text);
      cursor: pointer;
    }
    .video-card:hover {
      background: white;
      transform: translateY(-4px);
      box-shadow: 0 12px 32px rgba(15, 23, 42, 0.1);
      border-color: rgba(22, 101, 52, 0.3);
    }
    .video-card-thumb {
      width: 100%;
      aspect-ratio: 16 / 9;
      position: relative;
      background: #e2e8f0;
      overflow: hidden;
    }
    .video-card-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }
    .video-card-thumb::after {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.15);
      transition: background 0.3s ease;
    }
    .video-card-play {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.9);
      width: 56px;
      height: 56px;
      background: rgba(255, 255, 255, 0.95);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-primary);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      z-index: 2;
      box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .video-card:hover .video-card-thumb::after {
      background: rgba(0,0,0,0.4);
    }
    .video-card:hover .video-card-thumb img {
      transform: scale(1.05);
    }
    .video-card:hover .video-card-play {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }
    .video-card-content {
      padding: 16px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .video-no {
      background: var(--color-primary);
      color: white;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      font-size: 0.9rem;
      flex-shrink: 0;
    }
    .video-name {
      font-weight: 600;
      line-height: 1.3;
    }

    /* Modal Styles */
    .video-modal {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.95);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
      backdrop-filter: blur(12px);
    }
    .video-modal.is-open {
      opacity: 1;
      pointer-events: auto;
    }
    .video-modal-content {
      position: relative;
      width: 100%;
      max-width: 1000px;
      aspect-ratio: 16 / 9;
      background: black;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 32px 64px rgba(0,0,0,0.5);
      transform: scale(0.95) translateY(20px);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .video-modal.is-open .video-modal-content {
      transform: scale(1) translateY(0);
    }
    .video-modal iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
    .video-modal-close {
      position: absolute;
      top: 24px;
      right: 24px;
      background: rgba(255,255,255,0.1);
      color: white;
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 50%;
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 1001;
      transition: all 0.2s ease;
    }
    .video-modal-close:hover {
      background: white;
      color: black;
      transform: scale(1.1);
    }
  </style>
</head>
<body>
  <div data-layout-slot="header"></div>

  <main class="main-content">
    <section class="section">
      <div class="container">
        <header class="section-header">
          <p class="section-eyebrow">Championship</p>
          <h1 class="section-title">Syllabus &amp; Guidelines Videos</h1>
          <p class="section-description">Watch the instructional videos for the State Yoga Championship syllabus.</p>
        </header>

        <div class="videos-grid">
"""

for v in videos:
    new_html += f"""          <div class="video-card" data-video-id="{v['id']}">
            <div class="video-card-thumb">
              <img src="https://img.youtube.com/vi/{v['id']}/hqdefault.jpg" alt="{v['name']}" loading="lazy" />
              <div class="video-card-play">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="5 3 19 12 5 21 5 3"></polygon>
                </svg>
              </div>
            </div>
            <div class="video-card-content">
              <span class="video-no">{v['no']}</span>
              <span class="video-name">{v['name']}</span>
            </div>
          </div>\n"""

new_html += """        </div>
      </div>
    </section>
  </main>

  <div class="video-modal" id="videoModal">
    <button class="video-modal-close" id="videoModalClose" aria-label="Close video">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>
    <div class="video-modal-content" id="videoModalContent">
      <!-- Iframe injected here via JS -->
    </div>
  </div>

  <div data-layout-slot="footer"></div>
  <script src="assets/js/main.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const modal = document.getElementById('videoModal');
      const modalContent = document.getElementById('videoModalContent');
      const closeBtn = document.getElementById('videoModalClose');
      const cards = document.querySelectorAll('.video-card');

      function openModal(videoId) {
        modalContent.innerHTML = `<iframe src="https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
        modal.classList.add('is-open');
        document.body.style.overflow = 'hidden';
      }

      function closeModal() {
        modal.classList.remove('is-open');
        document.body.style.overflow = '';
        setTimeout(() => {
          modalContent.innerHTML = '';
        }, 300);
      }

      cards.forEach(card => {
        card.addEventListener('click', () => {
          const videoId = card.getAttribute('data-video-id');
          if (videoId) openModal(videoId);
        });
      });

      closeBtn.addEventListener('click', closeModal);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
      });
    });
  </script>
</body>
</html>
"""

with open(html_path, 'w') as f:
    f.write(new_html)

print("Updated video cards and added modal logic!")
