import {
  ChangeDetectionStrategy,
  Component,
  inject,
  Input,
  TemplateRef,
  ViewEncapsulation,
} from '@angular/core';
import { NgbOffcanvas } from '@ng-bootstrap/ng-bootstrap';
import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';
import { RealEstateProperty } from '../../interfaces/realEstateProperty';

@Component({
  selector: 'app-search-form',
  standalone: true,
  imports: [NgbDropdownModule],
  templateUrl: './searchForm.component.html',
  styleUrl: './searchForm.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
  encapsulation: ViewEncapsulation.None,
})
export class SearchFormComponent {
  private offcanvasService = inject(NgbOffcanvas);
  @Input() properties: RealEstateProperty[] | null = null;

  openEnd(content: TemplateRef<any>) {
    this.offcanvasService.open(content, { position: 'end' });
  }
}
