import {
  ChangeDetectionStrategy,
  Component,
  inject,
  TemplateRef,
  ViewEncapsulation,
} from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DetailsComponent } from '../details/details.component';

@Component({
  selector: 'app-list',
  standalone: true,
  imports: [DetailsComponent],
  templateUrl: './list.component.html',
  styleUrl: './list.component.css',
  // encapsulation: ViewEncapsulation.None,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ListComponent {
  private modalService = inject(NgbModal);

  openXl(content: TemplateRef<any>) {
    this.modalService.open(content, { size: 'xl' });
  }
}
