import { ChangeDetectionStrategy, Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-register-page',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './registerPage.component.html',
  styleUrl: './registerPage.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class RegisterPageComponent {
  registerForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.registerForm = this.fb.group({
      username: [''],
      email: ['', Validators.email],
      password: ['', Validators.minLength(6)],
      password2: ['', Validators.minLength(6)],
      phone: [''],
    });
  }

  onSubmit(): void {}
}
