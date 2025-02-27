import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-password-reset',
  standalone: true,
  imports: [],
  templateUrl: './password-reset.component.html',
  styleUrl: './password-reset.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PasswordResetComponent { }
