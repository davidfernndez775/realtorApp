import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CommentsFormComponent } from '../commentsForm/commentsForm.component';
import { CarouselComponent } from '../carousel/carousel.component';

@Component({
  selector: 'app-comments',
  standalone: true,
  imports: [CommentsFormComponent, CarouselComponent],
  templateUrl: './comments.component.html',
  styleUrl: './comments.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CommentsComponent {}
