import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./shared/layout/layout.component').then((c) => c.LayoutComponent),
    children: [
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
        path: 'properties',
        loadComponent: () =>
          import(
            './properties/layout/layoutProperties/layoutProperties.component'
          ).then((c) => c.LayoutPropertiesComponent),
      },
      {
        path: 'dashboard',
        loadComponent: () =>
          import('./dashboard/pages/dashboard/dashboard.component').then(
            (c) => c.DashboardComponent
          ),
      },
      {
        path: '',
        loadComponent: () =>
          import('./auth/layoutAuth/layoutAuth.component').then(
            (c) => c.LayoutAuthComponent
          ),
        children: [
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
              import(
                './auth/pages/resetPasswordPage/resetPasswordPage.component'
              ).then((c) => c.ResetPasswordPageComponent),
          },
          {
            path: 'confirm-password',
            loadComponent: () =>
              import(
                './auth/pages/confirmPassword/confirmPassword.component'
              ).then((c) => c.ConfirmPasswordComponent),
          },
        ],
      },
    ],
  },
  { path: '**', redirectTo: '', pathMatch: 'full' },
];
