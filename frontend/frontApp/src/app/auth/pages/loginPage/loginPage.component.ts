import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { RouterModule } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login-page',
  standalone: true,
  imports: [RouterModule, ReactiveFormsModule],
  templateUrl: './loginPage.component.html',
  styleUrl: './loginPage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LoginPageComponent {
  private fb = inject(FormBuilder);
  private authService = inject(AuthService);

  public loginForm: FormGroup = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
  });

  login() {
    const { email, password } = this.loginForm.value;
    this.authService.login(email, password).subscribe({
      next: () => console.log('todo bien'),
      error: (error) => console.log({ loginError: error }),
    });
    // console.log(this.loginForm.value);
  }
}
