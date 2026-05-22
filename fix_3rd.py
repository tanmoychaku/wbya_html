import re

HTML = """
          <!-- Boys -->
          <div class="category-card">
            <h3 class="category-title">BOYS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Swapan Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Bhaskar K.</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Motilal Saha</div></div>
              </div>
            </div>
          </div>

          <!-- Girls -->
          <div class="category-card">
            <h3 class="category-title">GIRLS</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Souma Saha</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Kalyani Maity</div></div>
              </div>
            </div>
          </div>

          <!-- Boys <16 -->
          <div class="category-card">
            <h3 class="category-title">BOYS &lt;16</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Dipak Dutta</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Samir Samanta</div></div>
              </div>
            </div>
          </div>

          <!-- Girls <16 -->
          <div class="category-card">
            <h3 class="category-title">GIRLS &lt;16</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Smriti Sarma</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Poly Mukherjee</div></div>
              </div>
            </div>
          </div>

          <!-- Men -->
          <div class="category-card">
            <h3 class="category-title">MEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Swapan Roy</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Subrata Chakraborty</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Ranbir Singh</div></div>
              </div>
            </div>
          </div>

          <!-- Women -->
          <div class="category-card">
            <h3 class="category-title">WOMEN</h3>
            <div class="winners-list">
              <div class="winner-item">
                <div class="winner-rank rank-1">1st</div>
                <div class="winner-info"><div class="winner-name">Agamani Paul</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-2">2nd</div>
                <div class="winner-info"><div class="winner-name">Sovana Das</div></div>
              </div>
              <div class="winner-item">
                <div class="winner-rank rank-3">3rd</div>
                <div class="winner-info"><div class="winner-name">Shila Roy</div></div>
              </div>
            </div>
          </div>
"""

with open('results-3rd-national-yogasana-sports-championship.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'<div class="category-grid">.*?</div>\s*</div>\s*</section>', f'<div class="category-grid">{HTML}</div></div></section>', content, flags=re.DOTALL)

with open('results-3rd-national-yogasana-sports-championship.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
