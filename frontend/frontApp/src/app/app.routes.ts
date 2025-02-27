import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./home/pages/homePage/homePage.component').then(
        (c) => c.HomePageComponent
      ),
  },
  {
    path: 'about-us',
    loadComponent: () =>
      import('./home/pages/aboutUsPage/aboutUsPage.component').then(
        (c) => c.AboutUsPageComponent
      ),
  },
  {
    path: 'login',
    loadComponent: () =>
      import('./auth/pages/loginPage/loginPage.component').then(
        (c) => c.LoginPageComponent
      ),
  },
  {
    path: 'register',
    loadComponent: () =>
      import('./auth/pages/registerPage/registerPage.component').then(
        (c) => c.RegisterPageComponent
      ),
  },
  {
    path: 'reset-password',
    loadComponent: () =>
      import('./auth/pages/resetPasswordPage/resetPasswordPage.component').then(
        (c) => c.ResetPasswordPageComponent
      ),
  },
  { path: '**', redirectTo: '', pathMatch: 'full' },
];
