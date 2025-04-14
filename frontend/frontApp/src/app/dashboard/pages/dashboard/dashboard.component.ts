import { ChangeDetectionStrategy, Component } from '@angular/core';
import { FavoriteCardComponent } from '../../components/favoriteCard/favoriteCard.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [FavoriteCardComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DashboardComponent {}
