/**
 * Custom GitHub Button with Organization Star Count
 *
 * This script replaces Mintlify's default GitHub button with a custom one that:
 * - Shows the total organization star count from files.namastex.ai API
 * - Links to the organization instead of a single repository
 * - Updates the count every 5 minutes
 * - Uses localStorage for caching
 */

(function() {
  'use strict';

  const API_URL = 'https://files.namastex.ai/nmstx-git-status.json';
  const ORG_URL = 'https://github.com/namastexlabs';
  const UPDATE_INTERVAL = 5 * 60 * 1000; // 5 minutes

  /**
   * Create the custom GitHub button HTML
   */
  function createGitHubButton(stars = '...') {
    return `
      <a
        id="custom-github-button"
        href="${ORG_URL}"
        target="_blank"
        rel="noreferrer noopener"
        aria-label="GitHub organization with ${stars} stars"
      >
        <!-- GitHub Icon -->
        <span class="github-icon">
          <svg fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
          </svg>
        </span>

        <!-- Organization Name -->
        <span class="org-name">namastexlabs</span>

        <!-- Star Section (standalone group) -->
        <span class="star-section">
          <!-- Hollow Star Icon -->
          <svg class="star-icon" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
          </svg>

          <!-- Star Count -->
          <span class="star-count">${stars}</span>
        </span>
      </a>
    `;
  }

  /**
   * Fetch star count from API
   */
  async function fetchStars() {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      const stars = data.summary.total_stars;
      console.log('⭐ Fetched total stars:', stars);

      // Cache it
      localStorage.setItem('nmstx-stars', JSON.stringify({
        count: stars,
        timestamp: Date.now()
      }));

      return stars;
    } catch (error) {
      console.error('❌ Failed to fetch stars:', error);

      // Try to use cached value
      const cached = localStorage.getItem('nmstx-stars');
      if (cached) {
        const data = JSON.parse(cached);
        console.log('📦 Using cached stars:', data.count);
        return data.count;
      }

      return null;
    }
  }

  /**
   * Update existing button or inject new one
   */
  async function updateButton() {
    const stars = await fetchStars();
    if (!stars) return;

    const existingButton = document.getElementById('custom-github-button');

    if (existingButton) {
      // Just update the count
      const countElement = existingButton.querySelector('.star-count');
      if (countElement) {
        countElement.textContent = stars;
        console.log('✅ Updated star count to:', stars);
      }
    } else {
      // Inject the button
      injectButton(stars);
    }
  }

  /**
   * Inject the custom button into the navbar
   */
  function injectButton(stars) {
    console.log('🔍 Looking for navbar to inject button...');

    // Check if button already exists
    if (document.getElementById('custom-github-button')) {
      console.log('ℹ️ Custom button already exists, skipping injection');
      return true;
    }

    // Find the navbar - try multiple selectors
    const selectors = [
      'nav ul', // Main nav list
      'header nav',
      '[role="navigation"]',
      '.navbar',
      'nav'
    ];

    let navbar = null;
    for (const selector of selectors) {
      navbar = document.querySelector(selector);
      if (navbar) {
        console.log('✅ Found navbar:', selector);
        break;
      }
    }

    if (!navbar) {
      console.log('❌ Navbar not found yet, will retry...');
      return false;
    }

    // Create a list item container
    const li = document.createElement('li');
    li.className = 'custom-github-li';
    li.innerHTML = createGitHubButton(stars);

    // Append to navbar
    navbar.appendChild(li);
    console.log('✅ Custom GitHub button injected with', stars, 'stars');

    return true;
  }

  /**
   * Initialize
   */
  function init() {
    console.log('🎬 Initializing custom GitHub button...');

    // Try to inject immediately
    setTimeout(async () => {
      const stars = await fetchStars() || '260';

      if (!injectButton(stars)) {
        // Retry after delay
        setTimeout(async () => {
          const retryStars = await fetchStars() || '260';
          if (!injectButton(retryStars)) {
            console.log('⏰ Button injection failed, will wait for DOM changes');
          }
        }, 1000);
      }
    }, 500);

    // Watch for DOM changes
    const observer = new MutationObserver(() => {
      if (!document.getElementById('custom-github-button')) {
        const cachedData = localStorage.getItem('nmstx-stars');
        const stars = cachedData ? JSON.parse(cachedData).count : '260';
        injectButton(stars);
      }
    });

    if (document.body) {
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    }

    // Periodic updates
    setInterval(updateButton, UPDATE_INTERVAL);

    console.log('✅ Custom GitHub button script initialized');
  }

  // Start when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
