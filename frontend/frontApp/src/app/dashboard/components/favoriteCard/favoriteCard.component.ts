import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-favorite-card',
  standalone: true,
  imports: [],
  templateUrl: './favoriteCard.component.html',
  styleUrl: './favoriteCard.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FavoriteCardComponent { }
