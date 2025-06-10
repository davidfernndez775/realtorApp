import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnInit,
  TemplateRef,
  OnChanges,
  SimpleChanges,
} from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbCarouselModule } from '@ng-bootstrap/ng-bootstrap';
import { TableDetailsComponent } from '../tableDetails/tableDetails.component';
import {
  RealEstateProperty,
  RealEstatePropertyImages,
} from '../../interfaces/realEstatePropertyinterface.';
import { catchError, map, Observable, of, startWith, tap } from 'rxjs';
import { RealEstatePropertyService } from '../../services/realEstateProperty.service';

// To handle the options to visualize the cards
interface ImageState {
  loading: boolean;
  error: string | null;
  images: RealEstatePropertyImages[] | null;
}

@Component({
  selector: 'app-details',
  standalone: true,
  imports: [CommonModule, NgbCarouselModule, TableDetailsComponent],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DetailsComponent implements OnChanges {
  @Input() property!: RealEstateProperty;
  public state$!: Observable<ImageState>;
  // images = [944, 1011, 984].map((n) => `https://picsum.photos/id/${n}/900/500`);
  public images: string[] = [];

  constructor(private realEstatePropertyService: RealEstatePropertyService) {}

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['property'] && this.property) {
      // console.log('⚡ property recibido:', this.property); // <-- DEBUG

      this.state$ = this.realEstatePropertyService
        .getPropertyImages(this.property.id)
        .pipe(
          map((images) => {
            // console.log('✅ Petición exitosa, imágenes:', images); // 👈 LOG 1
            return {
              loading: false,
              error: null,
              images: images,
            };
          }),
          tap((state) => {
            this.images = state.images?.map((img) => img.image) || [];
            // console.log('🧩 this.images:', this.images); // 👈 LOG 2
          }),
          startWith({
            loading: true,
            error: null,
            images: null,
          }),
          catchError((error) => {
            // console.error('❌ Error al cargar imágenes:', error); // 👈 LOG 3
            return of({
              loading: false,
              error: 'Error loading images.',
              images: null,
            });
          })
        );
    }
  }
}
