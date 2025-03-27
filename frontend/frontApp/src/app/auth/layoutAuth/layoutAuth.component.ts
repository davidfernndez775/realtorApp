import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-layout-auth',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './layoutAuth.component.html',
  styleUrl: './layoutAuth.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LayoutAuthComponent {}
