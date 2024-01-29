import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
await page.goto('http://localhost:5173/');
await 1000;
await page.waitForLoadState('networkidle');
});


test('Ajout du todo', async ({ page }) => {
await page.locator('#task').click();
await page.locator('#task').fill('Test');
await page.locator('#task').press('Enter');
await page.getByRole('button', { name: 'Ajouter' }).click();
});


test('Ajouter des todos et les compléter', async ({ page }) => {
    await page.locator('#task').click();
    for(let i = 1; i < 6; i++) { // Remplacez 5 par le nombre de fois que vous voulez répéter le test
        await page.locator('#task').click();
        await page.locator('#task').fill('Test ' + i);
        await page.locator('#task').press('Enter');
        await page.getByRole('button', { name: 'Ajouter' }).click();
}
    for (let i = 0; i < 5; i++) {
        await page.waitForTimeout(1000);
        await page.locator('input[type="checkbox"][name="task' + i + '"]').click();
}
});




test('Ajouter 5 todos', async ({ page }) => {
    await page.locator('#task').click();
for(let i = 1; i < 6; i++) { // Remplacez 5 par le nombre de fois que vous voulez répéter le test
        await page.locator('#task').click();
        await page.locator('#task').fill('Test ' + i);
        await page.locator('#task').press('Enter');
        await page.getByRole('button', { name: 'Ajouter' }).click();
}
// supprimer le todo 4
await page.locator('button[name="toDelete3"]').click();
});