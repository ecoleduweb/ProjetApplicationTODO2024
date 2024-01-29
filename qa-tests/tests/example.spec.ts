import { test, expect } from '@playwright/test';

test('Verify all System', async ({ page }) => {
  await page.goto('https://status.rinogamache.ca/status/server/');

  // Get the text content of the body
  const bodyText = await page.textContent('body');

  // Expect the body "to contain" a substring.
  expect(bodyText).toContain('All Systems Operational');
});

test('get started link', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  // Click the get started link.
  await page.getByRole('link', { name: 'Get started' }).click();

  // Expects page to have a heading with the name of Installation.
  await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
});
