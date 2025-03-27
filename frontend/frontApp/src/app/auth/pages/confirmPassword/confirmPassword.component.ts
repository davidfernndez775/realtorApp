import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-confirm-password',
  standalone: true,
  imports: [],
  templateUrl: './confirmPassword.component.html',
  styleUrl: './confirmPassword.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ConfirmPasswordComponent { }
