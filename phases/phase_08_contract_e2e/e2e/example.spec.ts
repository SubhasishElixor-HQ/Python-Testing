import { test, expect } from "@playwright/test";

// Template only: adapt URL and selectors to a real frontend.
test("example page displays a heading", async ({ page }) => {
  await page.goto("http://127.0.0.1:3000/");
  await expect(page.getByRole("heading")).toBeVisible();
});
