import re

HTML = """
          <!-- Boys -->
          <div class="category-card">
            <h3 class="category-title">BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Subir Roy</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Goutam Bose</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Uddolok Roy</div></div>
              </div>
            </div>
          </div>

          <!-- Girls -->
          <div class="category-card">
            <h3 class="category-title">GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Khana Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Smriti Sarma</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Lipika Biswas</div></div>
              </div>
            </div>
          </div>

          <!-- Men -->
          <div class="category-card">
            <h3 class="category-title">MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Himadri Chatterjee</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Jyotiprokash Nandi</div></div>
              </div>
            </div>
          </div>

          <!-- Women -->
          <div class="category-card">
            <h3 class="category-title">WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Jhunu Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Jharna Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Namita Ghosh</div></div>
              </div>
            </div>
          </div>
"""

with open('results-1st-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the category-grid contents with our hardcoded perfect HTML
new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-1st-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
