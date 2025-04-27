import {
  ChangeDetectionStrategy,
  Component,
  inject,
  Input,
  OnInit,
  TemplateRef,
  ViewEncapsulation,
} from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DetailsComponent } from '../details/details.component';
import { RealEstatePropertyList } from '../../interfaces/realEstateProperty';
import { RealEstatePropertyService } from '../../services/realEstateProperty.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Observable, of } from 'rxjs';
import { catchError, map, startWith } from 'rxjs/operators';

// To handle the options to visualize the cards
interface ListState {
  loading: boolean;
  error: string | null;
  properties: RealEstatePropertyList[] | null;
}

@Component({
  selector: 'app-list',
  standalone: true,
  imports: [CommonModule, HttpClientModule, DetailsComponent],
  templateUrl: './list.component.html',
  styleUrl: './list.component.css',
  // encapsulation: ViewEncapsulation.None,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ListComponent implements OnInit {
  private modalService = inject(NgbModal);

  // public properties: RealEstatePropertyList[] = [];
  public state$!: Observable<ListState>;

  openXl(content: TemplateRef<any>) {
    this.modalService.open(content, { size: 'xl' });
  }

  constructor(private realEstatePropertyService: RealEstatePropertyService) {}

  ngOnInit(): void {
    this.state$ = this.realEstatePropertyService.getPropertyList().pipe(
      map((properties) => ({
        loading: false,
        error: null,
        properties,
      })),
      startWith({
        loading: true,
        error: null,
        properties: null,
      }),
      catchError((error) =>
        of({
          loading: false,
          error: 'Failed to load properties.',
          properties: null,
        })
      )
    );
  }
}
