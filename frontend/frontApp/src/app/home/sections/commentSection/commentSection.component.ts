import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CommentsFormComponent } from '../../components/commentsForm/commentsForm.component';
import { CarouselComponent } from '../../components/carousel/carousel.component';

@Component({
  selector: 'app-comment-section',
  standalone: true,
  imports: [CommentsFormComponent, CarouselComponent],
  templateUrl: './commentSection.component.html',
  styleUrl: './commentSection.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CommentSectionComponent {}
