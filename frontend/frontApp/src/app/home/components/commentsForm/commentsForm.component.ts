import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-comments-form',
  standalone: true,
  imports: [],
  templateUrl: './commentsForm.component.html',
  styleUrl: './commentsForm.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CommentsFormComponent { }
