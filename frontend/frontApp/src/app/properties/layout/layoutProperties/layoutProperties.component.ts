import { ChangeDetectionStrategy, Component } from '@angular/core';
import { NgbNavModule } from '@ng-bootstrap/ng-bootstrap';
import { SearchFormComponent } from '../../components/searchForm/searchForm.component';
import { MapComponent } from '../../components/map/map.component';
import { ListComponent } from '../../components/list/list.component';
import { HttpClientModule } from '@angular/common/http';
import { RealEstateProperty } from '../../interfaces/realEstatePropertyinterface.';
import { catchError, map, Observable, of, startWith } from 'rxjs';
import { RealEstatePropertyService } from '../../services/realEstateProperty.service';
import { CommonModule } from '@angular/common';

// To handle the options to visualize the cards
interface ListState {
  loading: boolean;
  error: string | null;
  properties: RealEstateProperty[] | null;
}

@Component({
  selector: 'app-layout-properties',
  standalone: true,
  imports: [
    CommonModule,
    NgbNavModule,
    SearchFormComponent,
    MapComponent,
    ListComponent,
    HttpClientModule,
  ],
  templateUrl: './layoutProperties.component.html',
  styleUrl: './layoutProperties.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LayoutPropertiesComponent {
  public state$!: Observable<ListState>;

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
      catchError(() =>
        of({
          loading: false,
          error: 'Error loading properties.',
          properties: null,
        })
      )
    );
  }

  // function to filter properties by tabs
  filterProperties(
    properties: RealEstateProperty[] | null,
    type: 'for_sale' | 'for_rent'
  ): RealEstateProperty[] {
    if (!properties) return [];
    return properties.filter((p) => p.for_rent_or_sale === type);
  }

  onFiltersApplied(filters: any): void {
    this.state$ = this.realEstatePropertyService.getPropertyList(filters).pipe(
      map((properties) => ({
        loading: false,
        error: null,
        properties,
      })),
      startWith({ loading: true, error: null, properties: null }),
      catchError(() =>
        of({
          loading: false,
          error: 'Error loading properties.',
          properties: null,
        })
      )
    );
  }
}
